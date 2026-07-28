import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.models import resnet18
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
train_transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.RandomRotation(10),
    transforms.ToTensor()
])
train_dataset=datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=train_transform
)
train_loader=DataLoader(
    train_dataset,batch_size=64,shuffle=True
)
test_transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.Grayscale(num_output_channels=3),
    transforms.ToTensor()
])
test_dataset=datasets.MNIST(
    root="./data",
    train=False,
    download=True,
    transform=test_transform
)
test_loader=DataLoader(
    test_dataset,batch_size=64,shuffle=False
)
model=resnet18(weights="DEFAULT")
for param in model.parameters():
  param.requires_grad=False
model.fc=nn.Linear(512,10)
criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(
    model.fc.parameters(),lr=0.001
)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
for epoch in range(2):
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)
        output = model(images)
        loss = criterion(output, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")