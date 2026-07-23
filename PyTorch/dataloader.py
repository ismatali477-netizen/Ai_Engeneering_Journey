import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0]
])

y = torch.tensor([
    [10.0],
    [20.0],
    [30.0],
    [40.0],
    [50.0],
    [60.0]
])
dataset=TensorDataset(x,y)
loader=DataLoader(
    dataset,
    batch_size=3,
    shuffle=True
)
for batch_x,batch_y in loader:
  print(batch_x)
  print(batch_y)
  print("-----------------------")