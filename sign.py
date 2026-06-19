import json
import sys
from pathlib import Path
from nacl.signing import SigningKey

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

    sk = SigningKey((KEY_DIR / "private.key").read_bytes())
    pk = sk.verify_key

    cert.pop("signature", None)

    msg = canonical_bytes(cert)
    sig = sk.sign(msg).signature

    cert["signature"] = {
        "algorithm": "ed25519",
        "public_key": pk.encode().hex(),
        "signature": sig.hex()
    }

    cert_path.write_text(
        json.dumps(cert, sort_keys=True, separators=(",", ":"), ensure_ascii=False),
        encoding="utf-8"
    )
    print("Certificate signed successfully:", cert_path)

if __name__ == "__main__":
    main()
