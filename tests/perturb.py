import torch

# Load the original model
sd = torch.load("model.pth", map_location="cpu")

# Perturb just one tensor slightly
for name in sorted(sd.keys()):
    t = sd[name]
    if t.is_floating_point():
        sd[name] = t + torch.randn_like(t) * 1e-6
    break  # only perturb the first tensor

# Save the perturbed version
torch.save(sd, "model_perturbed.pth")
print("Saved perturbed model to model_perturbed.pth")