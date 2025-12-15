# aathman/keygen.py
from nacl.signing import SigningKey
from pathlib import Path
import os

# Keys stored in your home directory (ultra secure location)
KEY_DIR = Path.home() / ".aathman" / "keys"
KEY_DIR.mkdir(parents=True, exist_ok=True)

def main():
    # Generate Ed25519 keypair
    sk = SigningKey.generate()
    pk = sk.verify_key

    # Save private and public keys
    (KEY_DIR / "private.key").write_bytes(sk.encode())
    (KEY_DIR / "public.key").write_bytes(pk.encode())

    print("Keys generated securely in:", KEY_DIR)

if __name__ == "__main__":
    main()