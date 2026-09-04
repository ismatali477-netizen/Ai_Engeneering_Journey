import torch
import torch.nn as nn
import torch.optim as optim
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
# Create model
model = TinyCNN()
# Loss function
criterion = nn.CrossEntropyLoss()
# Optimizer
optimizer = optim.Adam(model.parameters(), lr=0.001)
# Fake training data
images = torch.randn(10, 3, 28, 28)
# Labels: 0 = CAT, 1 = DOG
labels = torch.tensor([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
# Training loop
for epoch in range(10):
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
    print(f"Epoch {epoch + 1}/10 | Loss: {loss.item():.4f}")