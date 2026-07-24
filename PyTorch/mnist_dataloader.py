import torch
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
transform=transforms.ToTensor()
train_dataset=datasets.MNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform
)
train_loader=DataLoader(
    train_dataset,
    batch_size=32,
    shuffle=True
)
print(len(train_dataset))
image, label = train_dataset[0]
print(image.shape)
print(label)
for images,labels in train_loader:
  print(images.shape)
  print(labels.shape)
  break