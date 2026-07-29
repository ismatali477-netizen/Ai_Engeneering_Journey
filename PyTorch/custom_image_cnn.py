import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
transform=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])
dataset=datasets.ImageFolder(
    root="./datasets",
    transform=transform
    )
loader=DataLoader(
    dataset,batch_size=4,
    shuffle=True
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
device = torch.device(
    "cuda"
    if torch.cuda.is_available()
    else "cpu"
)
model = model.to(device)
for epoch in range(5):
    running_loss = 0
    for images, labels in loader:
        images = images.to(device)
        labels = labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {running_loss/len(loader):.2f}")