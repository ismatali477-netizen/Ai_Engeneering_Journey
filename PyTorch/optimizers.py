import torch
import torch.nn as nn
import torch.optim as optim
model=nn.Linear(3,1)
x = torch.tensor([[2.0, 3.0, 4.0]])
y = torch.tensor([[10.0]])
criterion=nn.MSELoss()
optimizer=optim.Adam(model.parameters(),lr=0.001)
prediction=model(x)
loss=criterion(prediction,y)
optimizer.zero_grad()
loss.backward()
optimizer.step()
print(loss.item())