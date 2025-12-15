import json
import sys
from datetime import datetime, timezone
from fingerprint import compute_fingerprint
import torch

def build_certificate(model_path: str) -> dict:
    state_dict = torch.load(model_path, map_location="cpu")
    param_count = sum(v.numel() for v in state_dict.values())

    cert = {
        "version": "aathman-lite-v1",
        "fingerprint": compute_fingerprint(model_path),
        "fingerprint_method": "sha256-param-bytes-v1",
        "model_metadata": {
            "file": model_path,
            "parameter_count": param_count,
        },
        "created_at": datetime.now(timezone.utc).isoformat()
    }
    return cert


def dump_canonical_json(obj: dict) -> bytes:
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cert_build.py model_path")
        sys.exit(1)

    cert = build_certificate(sys.argv[1])
    out = sys.argv[1] + ".aathman.json"

    with open(out, "wb") as f:
        f.write(dump_canonical_json(cert))

    print("Certificate written to " + out)