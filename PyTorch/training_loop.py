import torch
import torch.nn as nn
import torch.optim as optim
model = nn.Linear(2,1)
x = torch.tensor([
    [1.0,2.0],
    [2.0,3.0],
    [3.0,4.0],
    [4.0,5.0]
])

y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0]
])
criterion=nn.MSELoss()
optimizer=optim.Adam(model.parameters(),lr=0.01)
for epoch in range(100):
  prediction=model(x)
  loss=criterion(prediction,y)
  optimizer.zero_grad()
  loss.backward()
  optimizer.step()
  if (epoch+1)%20==0:
    print(f"Epoch {epoch+1}: Loss = {loss.item():.2f}")
print(f"Final predict: {model(x)}")