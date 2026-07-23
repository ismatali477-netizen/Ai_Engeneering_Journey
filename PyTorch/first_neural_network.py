import torch
import torch.nn as nn
model=nn.Sequential(
    nn.Linear(3,6),
    nn.ReLU(),
    nn.Linear(6,2)
)
x=torch.rand(5,3)
output=model(x)
print(output)
print(output.shape)