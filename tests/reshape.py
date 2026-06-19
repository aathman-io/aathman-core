import torch

sd = torch.load("model.pth", map_location="cpu")

if "bias" in sd:
    b = sd["bias"]
    sd["bias"] = b.view(b.numel(), 1)  
torch.save(sd, "model_reshaped.pth")
print("Reshaped 'bias' and saved to model_reshaped.pth")
