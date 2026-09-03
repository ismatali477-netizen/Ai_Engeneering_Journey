import torch
import torch.nn as nn
# Fake RGB image
x = torch.randn(1, 3, 28, 28)
conv = nn.Conv2d(
    in_channels=3,
    out_channels=4,
    kernel_size=3
)
pool = nn.MaxPool2d(
    kernel_size=2,
    stride=2
)
print("Input:", x.shape)
x = conv(x)
print("After Conv:", x.shape)
x = torch.relu(x)
print("After ReLU:", x.shape)
x = pool(x)
print("After Pool:", x.shape)
x = x.view(x.size(0), -1)
print("After Flatten:", x.shape)