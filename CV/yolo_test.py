from ultralytics import YOLO
# Load a pretrained YOLO model
model = YOLO("yolo11n.pt")
# Run detection
results = model(r"C:\Users\Saruk meeya\Downloads\test.jpg")
# Display the result
results[0].show()