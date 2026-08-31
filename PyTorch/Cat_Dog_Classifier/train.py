import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import CatDogModel
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "datasets"
# -------------------------
# 1. Transformations for training images
# -------------------------
train_transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ToTensor()
])
# -------------------------
# 1. Transformations for test images
# -------------------------
# -------------------------
test_transform=transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])
# 2. Load datasets
# -------------------------
train_dataset = datasets.ImageFolder(
    DATASET_DIR/"train",
    transform=train_transform
)
test_dataset = datasets.ImageFolder(
    DATASET_DIR/"test",
    transform=test_transform
)
# -------------------------
# 3. Create DataLoaders
# -------------------------
train_loader = DataLoader(
    train_dataset,
    batch_size=16,
    shuffle=True
)
test_loader = DataLoader(
    test_dataset,
    batch_size=16,
    shuffle=False
)
# -------------------------
# 4. Create the model
# -------------------------
model = CatDogModel()
# -------------------------
# 5. Loss + optimizer
# -------------------------
loss_function = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
# -------------------------
# 6. Training
# -------------------------
epochs = 10
for epoch in range(epochs):
    model.train()
    total_loss = 0
    correct=0
    total=0
    for images, labels in train_loader:
        predictions = model(images)
        loss = loss_function(predictions, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        # Calculate training accuracy
        predicted_classes = torch.argmax(predictions,dim=1)
        total+=labels.size(0)
        correct += (predicted_classes == labels).sum().item()
    train_accuracy = 100 * correct / total
    print(
        f"Epoch {epoch + 1}/{epochs} | "
        f"Loss: {total_loss:.4f} | "
        f"Train Accuracy: {train_accuracy:.2f}%"
    )
# -------------------------
# 7. Evaluate the model
# -------------------------
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        predictions = model(images)
        predicted_classes = torch.argmax(
            predictions,
            dim=1
        )
        total += labels.size(0)
        correct += (
            predicted_classes == labels
        ).sum().item()
accuracy = 100 * correct / total
print(f"Test Accuracy: {accuracy:.2f}%")
# -------------------------
# 8. Save model
# -------------------------
torch.save(
    model.state_dict(),
    "cat_dog_model.pth"
)
print("Training complete!")