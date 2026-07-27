import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
from torchvision.models import resnet18
transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])
train_dataset=datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)
loader=DataLoader(
    train_dataset,batch_size=64,shuffle=True
)
model=resnet18(weights="DEFAULT")
for param in model.parameters():
  param.requires_grad=False
model.fc=nn.Linear(512,10)
criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(
    model.fc.parameters(),lr=0.001
)
running_loss=0
for epoch in range(2):
  for images,labels in loader:
    output=model(images)
    loss=criterion(output,labels)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    running_loss+=loss.item()
  print(f"Epoch {epoch+1}: Loss = {running_loss/len(loader):.3f}")