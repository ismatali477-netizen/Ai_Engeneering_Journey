import torch
from PIL import Image
from torchvision import transforms
from model import CatDogModel
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "cat_dog_model.pth"
IMAGE_PATH= BASE_DIR/"datasets"/"cat.jpg"
model=CatDogModel()
model.load_state_dict(
    torch.load(MODEL_PATH, map_location="cpu")
)
model.eval()
transform=transforms.Compose([
    transforms.Resize((128,128)),
    transforms.ToTensor()
])
image_path="cat.jpg"
image=Image.open(IMAGE_PATH).convert("RGB")
image=transform(image)
image=image.unsqueeze(0)
with torch.no_grad():
    output = model(image)
    prediction = torch.argmax(output, dim=1)
classes = ["cat", "dog"]
result = classes[prediction.item()]
print(f"Prediction: {result}")