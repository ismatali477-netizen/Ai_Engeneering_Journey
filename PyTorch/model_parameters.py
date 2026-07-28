import torch.nn as nn
from torchvision.models import resnet18
model=resnet18(weights="DEFAULT")
for param in model.parameters():
  param.requires_grad=False
model.fc=nn.Linear(512,10)
total_parameters = sum(
    param.numel()
    for param in model.parameters()
)
trainable_parameters = sum(
    param.numel()
    for param in model.parameters()
    if param.requires_grad
)
print(f"Total parameters: {total_parameters:,}")
print(f"Trainable parameters: {trainable_parameters:,}")