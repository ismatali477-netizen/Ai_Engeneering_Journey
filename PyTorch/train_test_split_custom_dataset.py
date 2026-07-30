import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader,random_split
transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])
dataset=datasets.ImageFolder(
    root="./dataset",
    transform=transform
    )
train_size=int(0.8*len(dataset))
test_size=len(dataset)-train_size
train_dataset,test_dataset=random_split(
    dataset,
    [train_size,test_size]
)
train_loader=DataLoader(
    train_dataset,
    batch_size=4,
    shuffle=True
)
test_loader=DataLoader(
    test_dataset,
    batch_size=4,
    shuffle=False
)
model = nn.Sequential(
    nn.Conv2d(3,16,3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(16,32,3),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Flatten(),
    nn.Linear(32*54*54,64),
    nn.ReLU(),
    nn.Linear(
        64,
        len(dataset.classes)
    )
)
criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(
    model.parameters(),
    lr=0.001
)
for epoch in range(5):
    running_loss = 0
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(train_loader):.2f}")
model.eval()
correct=0
total=0
with torch.no_grad():
  for images,labels in test_loader:
    outputs = model(images)
    _, predicted = torch.max(outputs, 1)
    total += labels.size(0)
    correct += (predicted == labels).sum().item()
accuracy=100* correct/total
print(f"Test Accuracy: {accuracy:.2f}%")