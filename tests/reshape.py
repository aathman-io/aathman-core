# aathman/tests/reshape.py
import torch

sd = torch.load("model.pth", map_location="cpu")
# If bias exists, reshape it (e.g., flatten to (5,1) or back)
if "bias" in sd:
    b = sd["bias"]
    sd["bias"] = b.view(b.numel(), 1)  # change shape while keeping values
torch.save(sd, "model_reshaped.pth")
print("Reshaped 'bias' and saved to model_reshaped.pth")