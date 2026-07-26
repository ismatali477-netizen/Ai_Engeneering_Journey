import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
transform=transforms.ToTensor()
train_dataset=datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)
loader=DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
)
model=nn.Sequential(
    nn.Conv2d(1,8,3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(1352,10)
)
criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(model.parameters(),lr=0.001)
for epoch in range(2):
  for images,labels in loader:
    output=model(images)
    loss=criterion(output,labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
  print(f"Epoch {epoch+1}: Loss = {loss.item():.2f}")