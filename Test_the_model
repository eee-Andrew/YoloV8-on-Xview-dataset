#simple script , opens a video I downloaded from youtube with cars on a highway , uses the model we trained before with Xview dataset and detects the cars

import os
import cv2
from ultralytics import YOLO

# Define video directory and paths
VIDEOS_DIR = os.path.join('.', 'videos')
video_path = r"C:\Users\eeean\OneDrive\Desktop\XviewYolo8\sample_video.mp4"
video_path_out = '{}_out.mp4'.format(video_path)

# Initialize video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get frame dimensions and initialize video writer
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    exit()

H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

# Load the YOLO model
model = YOLO(r"C:\Users\eeean\OneDrive\Desktop\xViewv11\yolo8n.pt")  # Load a custom model

threshold = 0.5

while ret:
    # Run the model on the current frame
    results = model(frame)[0]

    # Process the results
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            # Draw bounding box and label
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    # Write the processed frame to the output video
    out.write(frame)

    # Optionally display the frame in a window (for debugging)
    cv2.imshow('YOLO Object Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Read the next frame
    ret, frame = cap.read()

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Processing complete. Output saved to:", r"C:\Users\eeean\OneDrive\Desktop\XviewYolo8")
