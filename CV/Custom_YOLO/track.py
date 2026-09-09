from ultralytics import YOLO
import cv2
model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0)
line_y = 300
# Remember which side of the line each person was on
previous_positions = {}
entered = 0
exited = 0
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
    # Draw counting line
    cv2.line(
        frame,
        (0, line_y),
        (frame.shape[1], line_y),
        (255, 0, 0),
        3
    )
    if results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy()
        for box, track_id, class_id in zip(boxes, ids, classes):
            if results[0].names[int(class_id)] != "person":
                continue
            x1, y1, x2, y2 = box
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)
            track_id = int(track_id)
            # Current side of line
            if center_y < line_y:
                current_side = "above"
            else:
                current_side = "below"
            # First time seeing this person
            if track_id not in previous_positions:
                previous_positions[track_id] = current_side
            else:
                previous_side = previous_positions[track_id]
                # Above → below
                if previous_side == "above" and current_side == "below":
                    entered += 1
                # Below → above
                elif previous_side == "below" and current_side == "above":
                    exited += 1
                # Update position
                previous_positions[track_id] = current_side
            # Draw center
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )
            # Draw ID
            cv2.putText(
                frame,
                f"ID {track_id}",
                (int(x1), int(y1) - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )
    # Display counts
    cv2.putText(
        frame,
        f"Entered: {entered}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )
    cv2.putText(
        frame,
        f"Exited: {exited}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )
    cv2.imshow("YOLO Line Counter", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()