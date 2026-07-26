import torch.nn as nn
from torchvision.models import resnet18
model=resnet18(weights="DEFAULT")
model.fc=nn.Linear(512,10)
for param in model.parameters():
  param.requires_grad=False
model.fc.requires_grad_(True)
print(model.fc)