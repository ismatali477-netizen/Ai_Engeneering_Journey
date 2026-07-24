import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset,DataLoader
x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0],
    [7.0],
    [8.0]
])
y = torch.tensor([
    [3.0],
    [6.0],
    [9.0],
    [12.0],
    [15.0],
    [18.0],
    [21.0],
    [24.0]
])
dataset=TensorDataset(x,y)
loader=DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)
model=nn.Linear(1,1)
criterion=nn.MSELoss()
optimizer=optim.SGD(model.parameters(),lr=0.01)
for epoch in range(50):
  for batch_x,batch_y in loader:
    prediction=model(batch_x)
    loss=criterion(prediction,batch_y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
  if (epoch+1)%10==0:
    print(f"Epoch {epoch+1}: Loss= {loss.item():.2f}")
print(model(x))