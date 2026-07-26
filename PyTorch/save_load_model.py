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
train_loader=DataLoader(
    train_dataset,
    batch_size=64,
    shuffle=True
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
torch.save(model.state_dict(),"mnist_cnn.pth")
print("Model Saved Successfully!")
model = nn.Sequential(
    nn.Conv2d(1,8,3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(8,16,3),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(1936,10)
)
model.load_state_dict(torch.load("mnist_cnn.pth"))
model.eval()
print("Model Loaded Successfully!")