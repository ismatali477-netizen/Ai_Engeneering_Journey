from ultralytics import YOLO
model = YOLO("yolo11n.pt")
results = model(r"C:\Users\Saruk meeya\Downloads\test.jpg",conf=0.5)
result = results[0]
# Read every detected object
for box in result.boxes:
    class_id = int(box.cls[0])
    confidence = float(box.conf[0])
    coordinates = box.xyxy[0].tolist()
    class_name = result.names[class_id]
    print(
        f"Object: {class_name} | "
        f"Confidence: {confidence:.2f} | "
        f"Box: {coordinates}"
    )