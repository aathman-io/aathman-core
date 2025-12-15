# aathman/sign.py
import json
import sys
from pathlib import Path
from nacl.signing import SigningKey

# Keys read from your home directory (ultra secure location)
KEY_DIR = Path.home() / ".aathman" / "keys"

def canonical_bytes(obj: dict) -> bytes:
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False
    ).encode("utf-8")

def main():
    if len(sys.argv) != 2:
        print("Usage: python sign.py model.pth.aathman.json")
        sys.exit(1)

    cert_path = Path(sys.argv[1])
    cert = json.loads(cert_path.read_text(encoding="utf-8"))

    # Load private key
    sk = SigningKey((KEY_DIR / "private.key").read_bytes())
    pk = sk.verify_key

    # Remove old signature if re-signing
    cert.pop("signature", None)

    # Sign canonical JSON
    msg = canonical_bytes(cert)
    sig = sk.sign(msg).signature

    # Attach signature block
    cert["signature"] = {
        "algorithm": "ed25519",
        "public_key": pk.encode().hex(),
        "signature": sig.hex()
    }

    # Save updated certificate
    cert_path.write_text(
        json.dumps(cert, sort_keys=True, separators=(",", ":"), ensure_ascii=False),
        encoding="utf-8"
    )
    print("Certificate signed successfully:", cert_path)

if __name__ == "__main__":
    main()