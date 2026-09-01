import sys
from pathlib import Path
import torch
from PIL import Image
from torchvision import transforms
from model import CatDogModel
# -------------------------
# 1. Device
# -------------------------
device = torch.device("cpu")
# -------------------------
# 2. Load model
# -------------------------
model = CatDogModel()
model.load_state_dict(
    torch.load(
        Path(__file__).resolve().parent / "cat_dog_model.pth",
        map_location=device
    )
)
model.to(device)
model.eval()
# -------------------------
# 3. Image transformation
# -------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])
# -------------------------
# 4. Get image path
# -------------------------
if len(sys.argv) < 2:
    print("Usage:")
    print("python predict.py path_to_image.jpg")
    sys.exit()
image_path = Path(sys.argv[1])
# -------------------------
# 5. Load image
# -------------------------
image = Image.open(image_path).convert("RGB")
image = transform(image)
image = image.unsqueeze(0)
image = image.to(device)
# -------------------------
# 6. Prediction
# -------------------------
with torch.no_grad():
    output = model(image)
    probabilities = torch.softmax(
        output,
        dim=1
    )
    confidence, predicted = torch.max(
        probabilities,
        dim=1
    )
# -------------------------
# 7. Result
# -------------------------
classes = ["cats", "dogs"]
prediction = classes[predicted.item()]
confidence = confidence.item() * 100
print()
print(f"Prediction: {prediction.upper()}")
print(f"Confidence: {confidence:.2f}%")