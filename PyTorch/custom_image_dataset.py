from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])
dataset = datasets.ImageFolder(
    root="./datasets",
    transform=transform
)
loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)
print("Classes:", dataset.classes)
print("Class labels:", dataset.class_to_idx)
images, labels = next(iter(loader))
print("Image batch shape:", images.shape)
print("Labels:", labels)