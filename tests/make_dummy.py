import torch
import torch.nn as nn

model = nn.Linear(10, 5)
torch.save(model.state_dict(), "model.pth")
print("Saved dummy model to model.pth")