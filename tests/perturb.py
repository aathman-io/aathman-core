import torch

sd = torch.load("model.pth", map_location="cpu")

for name in sorted(sd.keys()):
    t = sd[name]
    if t.is_floating_point():
        sd[name] = t + torch.randn_like(t) * 1e-6
    break  

torch.save(sd, "model_perturbed.pth")
print("Saved perturbed model to model_perturbed.pth")
