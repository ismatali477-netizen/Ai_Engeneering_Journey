import torch
import torch.nn as nn
prediction = torch.tensor([7.5])
target = torch.tensor([8.0])
criterion=nn.MSELoss()
loss=criterion(prediction,target)
print(loss)
prediction=torch.tensor([[1.2, 2.8]])
target = torch.tensor([1])
criterion=nn.CrossEntropyLoss()
loss=criterion(prediction,target)
print(loss)