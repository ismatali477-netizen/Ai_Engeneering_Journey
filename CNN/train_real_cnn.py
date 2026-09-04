import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
# Image transformations
transform = transforms.Compose([
    transforms.Resize((28, 28)),
    transforms.ToTensor()
])
# Load training dataset
train_dataset = datasets.ImageFolder(
    "PyTorch/Cat_Dog_Classifier/datasets/train",
    transform=transform
)
# Create DataLoader
train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True
)
# -------------------------
# Tiny CNN
# -------------------------
class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 4, kernel_size=3)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)
        self.fc = nn.Linear(4 * 13 * 13, 2)
    def forward(self, x):
        x = self.conv(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
# -------------------------
# Model setup
# -------------------------
model = TinyCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)
# -------------------------
# Training
# -------------------------
epochs = 10
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0
    for images, labels in train_loader:
        # Forward pass
        outputs = model(images)
        # Calculate loss
        loss = criterion(outputs, labels)
        # Clear old gradients
        optimizer.zero_grad()
        # Backpropagation
        loss.backward()
        # Update weights
        optimizer.step()
        # Track loss
        running_loss += loss.item()
        # Track accuracy
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    print(
        f"Epoch {epoch + 1}/{epochs} | "
        f"Loss: {running_loss / len(train_loader):.4f} | "
        f"Accuracy: {accuracy:.2f}%"
    )