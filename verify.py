# aathman/verify.py

import json
import sys
import torch
from pathlib import Path
from nacl.signing import VerifyKey
from fingerprint import compute_fingerprint


def canonical_bytes(obj: dict) -> bytes:
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")


def verify_signature(cert: dict) -> None:
    sig_block = cert.get("signature")
    if not sig_block:
        raise ValueError("Missing signature")

    vk = VerifyKey(bytes.fromhex(sig_block["public_key"]))
    sig = bytes.fromhex(sig_block["signature"])

    unsigned = dict(cert)
    unsigned.pop("signature", None)

    vk.verify(canonical_bytes(unsigned), sig)


def diff_blocks(path_a: str, path_b: str, blocks=8):
    a = torch.load(path_a, map_location="cpu")
    b = torch.load(path_b, map_location="cpu")

    diffs = []
    for k in sorted(a.keys()):
        ta = a[k].detach().cpu().float().view(-1)
        tb = b[k].detach().cpu().float().view(-1)
        n = min(len(ta), len(tb))
        if n == 0:
            continue

        step = max(1, n // blocks)
        for i in range(0, n, step):
            da = ta[i:i + step]
            db = tb[i:i + step]
            delta = torch.norm(da - db).item()
            diffs.append((k, i, delta))

    diffs.sort(key=lambda x: x[2], reverse=True)
    return diffs[:5]


# -----------------------------
# Library API for PaCM
# -----------------------------

def verify_model(model_path: str, cert_path: str) -> dict:
    cert = json.loads(Path(cert_path).read_text(encoding="utf-8"))

    # Signature verification
    try:
        verify_signature(cert)
        signature_valid = True
    except Exception:
        signature_valid = False

    # Fingerprint verification
    recomputed = compute_fingerprint(model_path)
    expected = cert.get("fingerprint")
    fingerprint_match = recomputed == expected

    return {
        "signature_valid": signature_valid,
        "fingerprint_match": fingerprint_match,
        "signer_public_key": cert.get("signature", {}).get("public_key"),
        "parameter_count": cert.get("model_metadata", {}).get("parameter_count"),
        "valid": signature_valid and fingerprint_match,
    }


# -----------------------------
# CLI entrypoint (unchanged)
# -----------------------------

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python verify.py model.pth model.pth.aathman.json")
        sys.exit(1)

    model_path = sys.argv[1]
    cert_path = Path(sys.argv[2])

    cert = json.loads(cert_path.read_text(encoding="utf-8"))

    # Step 4A: verify signature
    try:
        verify_signature(cert)
    except Exception:
        print("FAIL: invalid signature")
        sys.exit(2)

    # Step 4B: recompute fingerprint
    recomputed = compute_fingerprint(model_path)
    expected = cert["fingerprint"]

    if recomputed == expected:
        print("PASS: model verified")
        sys.exit(0)

    # Step 4C: diagnostics
    print("FAIL: fingerprint mismatch")
    print("Diagnostics (top changes):")

    original_path = cert["model_metadata"]["file"]
    if Path(original_path).exists():
        for k, idx, d in diff_blocks(original_path, model_path):
            print(f"  {k} @ {idx}: Δ={d:.6f}")
    else:
        print("  original model file not found for diagnostics")

    sys.exit(3)    
