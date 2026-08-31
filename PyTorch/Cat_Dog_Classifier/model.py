import torch.nn as nn
from torchvision import models
class CatDogModel(nn.Module):
    def __init__(self, num_classes=2):
        super().__init__()
        # Load a pretrained ResNet18
        self.model = models.resnet18(
            weights=models.ResNet18_Weights.DEFAULT
        )
        # Freeze the pretrained layers
        for parameter in self.model.parameters():
            parameter.requires_grad = False
        # Replace the final layer
        self.model.fc = nn.Linear(
            self.model.fc.in_features,
            num_classes
        )
    def forward(self, x):
        return self.model(x)