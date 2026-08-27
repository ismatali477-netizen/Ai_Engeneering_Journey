import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import CatDogModel
# 1. Prepare the images
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])
# 2. Load the dataset
dataset = datasets.ImageFolder(
    "dataset",
    transform=transform
)
# 3. Create batches
loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)
# 4. Create the model
model = CatDogModel()
# 5. Loss function
loss_function = torch.nn.CrossEntropyLoss()
# 6. Optimizer
optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)
# 7. Training
epochs = 10
for epoch in range(epochs):
    total_loss = 0
    for images, labels in loader:
        # Forward pass
        predictions = model(images)
        # Calculate loss
        loss = loss_function(predictions, labels)
        # Clear old gradients
        optimizer.zero_grad()
        # Backpropagation
        loss.backward()
        # Update weights
        optimizer.step()
        total_loss += loss.item()
    print(
        f"Epoch {epoch + 1}/{epochs}, "
        f"Loss: {total_loss:.4f}"
    )
# 8. Save the trained model
torch.save(
    model.state_dict(),
    "cat_dog_model.pth"
)
print("Training complete!")