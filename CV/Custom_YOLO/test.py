from ultralytics import YOLO
# Load our custom-trained model
model = YOLO(r"runs\detect\train-2\weights\best.pt")
# Test image
results = model(
    r"C:\Users\Saruk meeya\Downloads\test.jpg",
    conf=0.5
)
# Display predictions
results[0].show()
# Print predictions
for box in results[0].boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    class_name = results[0].names[class_id]
    print(f"Object: {class_name} | Confidence: {confidence:.2f}")