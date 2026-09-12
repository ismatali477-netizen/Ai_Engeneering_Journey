from ultralytics import YOLO
import cv2
import math
model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)
previous_positions = {}
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to access webcam")
        break
    results = model.track(
        frame,
        conf=0.2,
        persist=True
    )
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy()
        for box, track_id, class_id in zip(boxes, ids, classes):
            if results[0].names[int(class_id)] != "person":
                continue
            x1, y1, x2, y2 = map(int, box)
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            track_id = int(track_id)
            movement = 0
            if track_id in previous_positions:
                old_x, old_y = previous_positions[track_id]
                movement = math.sqrt(
                    (center_x - old_x) ** 2 +
                    (center_y - old_y) ** 2
                )
            previous_positions[track_id] = (center_x, center_y)
            # Draw bounding box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )
            # Draw ID above the box
            cv2.putText(
                frame,
                f"ID: {track_id}",
                (x1, max(y1 - 30, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )
            # Draw movement below the ID
            cv2.putText(
                frame,
                f"Movement: {movement:.1f}px",
                (x1, max(y1 - 5, 45)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )
            # Draw center point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )
    cv2.imshow("Object Movement", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()