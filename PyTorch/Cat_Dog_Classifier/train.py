import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import CatDogModel
from sklearn.metrics import confusion_matrix, classification_report
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "datasets"
# -------------------------
# 1. Transformations for training images
# -------------------------
train_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
# -------------------------
# 1. Transformations for test images
# -------------------------
# -------------------------
test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
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
    lr=0.0001
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
# 8. Confusion Matrix
# -------------------------
all_predictions = []
all_labels = []
model.eval()
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        predictions = torch.argmax(
            outputs,
            dim=1
        )
        all_predictions.extend(
            predictions.cpu().numpy()
        )
        all_labels.extend(
            labels.cpu().numpy()
        )
# Create confusion matrix
cm = confusion_matrix(
    all_labels,
    all_predictions
)
print("\nConfusion Matrix:")
print(cm)
# Detailed report
print("\nClassification Report:")
print(
    classification_report(
        all_labels,
        all_predictions,
        target_names=test_dataset.classes
    )
)
# -------------------------
# Save the trained model
# -------------------------
model_path = BASE_DIR / "cat_dog_model.pth"
torch.save(
    model.state_dict(),
    model_path
)
print(f"Model saved to: {model_path}")
print("Training complete!")