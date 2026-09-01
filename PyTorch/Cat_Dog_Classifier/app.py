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
    try:
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
        # Prepare image
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
        cat_probability = probabilities[0][0].item() * 100
        dog_probability = probabilities[0][1].item() * 100
        confidence, predicted = torch.max(
            probabilities,
            dim=1
        )
        classes = ["CAT", "DOG"]
        prediction = classes[predicted.item()]
        confidence = confidence.item() * 100
        # Display result
        result_label.config(
            text=f"Prediction: {prediction}\n"
                 f"Confidence: {confidence:.2f}%"
        )
        probability_label.config(
            text=f"Cat: {cat_probability:.2f}%    "
                 f"Dog: {dog_probability:.2f}%"
        )
    except Exception as error:
        messagebox.showerror(
            "Error",
            f"Could not process this image.\n\n{error}"
        )
# Reset function
def reset():
    image_label.config(
        image="",
        text="Your image will appear here"
    )
    image_label.image = None
    result_label.config(
        text="Prediction: --\nConfidence: --"
    )
    probability_label.config(
        text="Cat: --%    Dog: --%"
    )
# Create window
root = tk.Tk()
root.title("Cat-Dog AI Classifier")
root.geometry("600x700")
root.resizable(False, False)
# Title
title_label = tk.Label(
    root,
    text="Cat-Dog AI",
    font=("Arial", 26, "bold")
)
title_label.pack(pady=(25, 5))
subtitle_label = tk.Label(
    root,
    text="Powered by ResNet18",
    font=("Arial", 11)
)
subtitle_label.pack(pady=(0, 15))
# Image display
image_label = tk.Label(
    root,
    text="Your image will appear here",
    font=("Arial", 12),
    width=40,
    height=15
)
image_label.pack(pady=10)
# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)
select_button = tk.Button(
    button_frame,
    text="Select Image",
    font=("Arial", 14, "bold"),
    padx=20,
    pady=8,
    command=predict_image
)
select_button.pack(side=tk.LEFT, padx=10)
reset_button = tk.Button(
    button_frame,
    text="Reset",
    font=("Arial", 14),
    padx=20,
    pady=8,
    command=reset
)
reset_button.pack(side=tk.LEFT, padx=10)
# Result
result_label = tk.Label(
    root,
    text="Prediction: --\nConfidence: --",
    font=("Arial", 20, "bold")
)
result_label.pack(pady=15)
# Probabilities
probability_label = tk.Label(
    root,
    text="Cat: --%    Dog: --%",
    font=("Arial", 13)
)
probability_label.pack(pady=5)
# Footer
footer_label = tk.Label(
    root,
    text="AI Engineering Project - Cat-Dog Image Classifier",
    font=("Arial", 9)
)
footer_label.pack(side=tk.BOTTOM, pady=15)
# Start application
root.mainloop()