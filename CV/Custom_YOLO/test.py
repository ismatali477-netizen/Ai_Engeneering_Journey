from ultralytics import YOLO
# Load our trained model
model = YOLO(
    r"runs\detect\train\weights\best.pt"
)
# Test image
results = model(
    r"C:\Users\Saruk meeya\Downloads\test.jpg",
    conf=0.5
)
# Display result
results[0].show()