import torch
from torch.utils.data import DataLoader
from torchvision import datasets,transforms
import torch.nn as nn
import torch.optim as optim

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
    nn.Flatten(),
    nn.Linear(28*28,64),
    nn.ReLU(),
    nn.Linear(64,10)
)
criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(model.parameters(),lr=0.001)
for epoch in range(2):
  for images,labels in loader:
    outputs=model(images)
    loss = criterion(outputs,labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
  print(f"Epoch {epoch+1}: Loss = {loss.item():.2f}")