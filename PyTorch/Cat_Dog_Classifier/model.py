import torch.nn as nn
class SimpleCNN(nn.Module):
  def __init__(self,num_classes):
    super().__init__()
    self.network=nn.Sequential(
        nn.Conv2d(3,16,3),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Conv2d(16,32,3),
        nn.ReLU(),
        nn.MaxPool2d(2),
        nn.Flatten(),
        nn.Linear(32*54*54,64),
        nn.ReLU(),
        nn.Linear(64,num_classes)
    )
  def forward(self,x):
    return self.network(x)