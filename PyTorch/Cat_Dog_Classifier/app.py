import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import torch
from PIL import Image, ImageTk
from torchvision import transforms
from model import CatDogModel
# -------------------------
# Model setup
# -------------------------
device = torch.device("cpu")
model = CatDogModel(num_classes=2)
model_path = Path(__file__).resolve().parent / "cat_dog_model.pth"
model.load_state_dict(
    torch.load(
        model_path,
        map_location=device
    )
)
model.to(device)
model.eval()
# -------------------------
# Image transformation
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
# Prediction function
# -------------------------
def predict_image():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[
            ("Image files", "*.jpg *.jpeg *.png *.webp"),
            ("All files", "*.*")
        ]
    )
    if not file_path:
        return
    image = Image.open(file_path).convert("RGB")
    # Display image
    preview = image.copy()
    preview.thumbnail((350, 350))
    photo = ImageTk.PhotoImage(preview)
    image_label.config(
        image=photo,
        text=""
    )
    image_label.image = photo
    # Prepare image for model
    input_image = transform(image)
    input_image = input_image.unsqueeze(0)
    input_image = input_image.to(device)
    # Prediction
    with torch.no_grad():
        output = model(input_image)
        probabilities = torch.softmax(
            output,
            dim=1
        )
        confidence, predicted = torch.max(
            probabilities,
            dim=1
        )
    classes = ["CAT", "DOG"]
    prediction = classes[predicted.item()]
    confidence = confidence.item() * 100
    result_label.config(
        text=f"Prediction: {prediction}\n"
             f"Confidence: {confidence:.2f}%"
    )
# -------------------------
# Create window
# -------------------------
root = tk.Tk()
root.title("Cat-Dog AI Classifier")
root.geometry("500x600")
title_label = tk.Label(
    root,
    text="🐱🐶 Cat-Dog AI",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=20)
select_button = tk.Button(
    root,
    text="Select Image",
    font=("Arial", 14),
    command=predict_image
)
select_button.pack(pady=10)
image_label = tk.Label(
    root,
    text="Your image will appear here",
    font=("Arial", 12)
)
image_label.pack(pady=20)
result_label = tk.Label(
    root,
    text="Prediction: --\nConfidence: --",
    font=("Arial", 18, "bold")
)
result_label.pack(pady=20)
root.mainloop()