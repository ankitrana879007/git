# Importing necessary libraries
import numpy as np          # Used for handling arrays and mathematical operations
import cv2                  # Used for computer vision tasks like image capture and object detection
import imutils              # Used for resizing and image processing
import datetime             # Used for time or date if needed later

# Load the cascade file for gun detection
gun_cascade = cv2.CascadeClassifier('cascade.xml')
if gun_cascade.empty():  # Check if the cascade file was loaded correctly
    print("Error: Could not load 'cascade.xml'. Make sure it’s in the same folder as this script.")
    exit()

# Start the webcam
camera = cv2.VideoCapture(0)
if not camera.isOpened():  # Check if the webcam opened properly
    print("Error: Could not open webcam.")
    exit()

# Variables to keep track of detection
gun_exist = False
prev_gun_exist = None

# Minimum area to ignore very small false detections
MIN_GUN_AREA = 60000

print("Press 'q' to quit.\n")

# Loop to continuously get frames from the webcam
while True:
    ret, frame = camera.read()  # Read one frame from the webcam
    if not ret:                 # If the frame could not be read, stop the loop
        print("Failed to grab frame from camera.")
        break

    frame = imutils.resize(frame, width=600)           # Resize the frame for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # Convert the frame to grayscale

    # Detect possible guns in the frame
    guns = gun_cascade.detectMultiScale(
        gray,                 # Input image
        scaleFactor=1.3,      # How much the image size is reduced at each scale
        minNeighbors=7,       # How many neighbors each rectangle should have to be kept
        minSize=(100, 100)    # Minimum size of detected object
    )

    gun_exist = False  # Assume no gun detected at first

    # Go through all detected objects
    for (x, y, w, h) in guns:
        area = w * h  # Calculate area of the detected object
        if area > MIN_GUN_AREA:  # If the area is large enough, it might be a gun
            gun_exist = True
            # Draw a green rectangle and label it as gun detected
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.putText(frame, "Gun Detected!", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            # If it is small, draw a thin yellow rectangle but do not mark as gun
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)

    # Print only when detection state changes
    if gun_exist != prev_gun_exist:
        if gun_exist:
            print("Gun detected")
        else:
            print("No gun detected")
        prev_gun_exist = gun_exist

    # Show the video feed
    cv2.imshow("Security Feed", frame)

    # Wait for a key press and check if 'q' is pressed to quit
    key = cv2.waitKey(20) & 0xFF
    if key == ord('q'):
        print("Closing camera...")
        break

# Release the camera and close all OpenCV windows
camera.release()
cv2.destroyAllWindows()
print("Camera closed.")