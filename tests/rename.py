# aathman/tests/rename.py
import torch

sd = torch.load("model.pth", map_location="cpu")
keys = sorted(sd.keys())
# Rename the first key deterministically
old = keys[0]
sd["renamed::" + old] = sd.pop(old)
torch.save(sd, "model_renamed.pth")
print(f"Renamed '{old}' -> 'renamed::{old}' and saved to model_renamed.pth")