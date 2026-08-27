import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
transform=transforms.ToTensor()
train_dataset=datasets.MNIST(
  root="./data",
  download=True,
  train=True,
  transform=transform
)
train_loader=DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)
test_dataset=datasets.MNIST(
  root="./data",
  train=False,
  transform=transform
)
test_loader=DataLoader(
    test_dataset,
    batch_size=64,
    shuffle=False
)
model=nn.Sequential(
    nn.Conv2d(1,8,3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(8,16,3),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(1936,10)
)
criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(
    model.parameters(),
    lr=0.001
)
for epoch in range(2):
  for images,labels in train_loader:
    output=model(images)
    loss=criterion(output,labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
model.eval()
correct=0
total=0
with torch.no_grad():
  for images,labels in test_loader:
    outputs=model(images)
    _,predicted=torch.max(outputs,1)
    total+=labels.size(0)
    correct+=(predicted==labels).sum().item()
Accuracy=100*correct/total
print(f"Accuracy: {Accuracy:.2f}%")