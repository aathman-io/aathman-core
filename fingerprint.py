# aathman/fingerprint.py
import sys
import hashlib
import torch
import numpy as np

def compute_fingerprint(model_path: str) -> str:
    state_dict = torch.load(model_path, map_location="cpu")
    byte_stream_parts = []

    # Deterministic order: sorted by parameter name
    for k in sorted(state_dict.keys()):
        t = state_dict[k].detach().cpu().numpy().astype("float32")

        # Header: name length + name + ndim + shape (big-endian int32)
        name_bytes = k.encode("utf-8")
        name_len = len(name_bytes).to_bytes(4, "big")
        ndim = len(t.shape).to_bytes(4, "big")
        shape_be = np.array(t.shape, dtype=">i4").tobytes()

        header = name_len + name_bytes + ndim + shape_be
        byte_stream_parts.append(header)

        # Body: canonical float32 bytes (little/big doesn’t matter once we choose; we choose float32)
        body = t.tobytes()
        byte_stream_parts.append(body)

    byte_stream = b"".join(byte_stream_parts)
    return hashlib.sha256(byte_stream).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fingerprint.py <model.pth>")
        sys.exit(1)

    fp = compute_fingerprint(sys.argv[1])
    print("Fingerprint:", fp)