import torch
import torch.nn as nn
class TinyCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(
            in_channels=3,
            out_channels=4,
            kernel_size=3
        )
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )
        self.fc = nn.Linear(4 * 13 * 13,2)
    def forward(self, x):
        x = self.conv(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
# Create model
model = TinyCNN()
# Fake RGB image
x = torch.randn(1, 3, 28, 28)
# Forward pass
output = model(x)
print("Input shape:", x.shape)
print("Output shape:", output.shape)
print("Raw output:", output)