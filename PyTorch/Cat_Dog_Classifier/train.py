import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import CatDogModel
# -------------------------
# 1. Image transformations
# -------------------------
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])
# -------------------------
# 2. Load datasets
# -------------------------
train_dataset = datasets.ImageFolder(
    "datasets/train",
    transform=transform
)
test_dataset = datasets.ImageFolder(
    "datasets/test",
    transform=transform
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

    for images, labels in train_loader:

        predictions = model(images)

        loss = loss_function(predictions, labels)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    print(
        f"Epoch {epoch + 1}/{epochs}, "
        f"Loss: {total_loss:.4f}"
    )


# -------------------------
# 7. Save model
# -------------------------

torch.save(
    model.state_dict(),
    "cat_dog_model.pth"
)

print("Training complete!")