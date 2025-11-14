import cv2

a = cv2.CascadeClassifier('frontalface.xml')

if a.empty():
    print("Error: Could not load 'frontalface.xml'. Make sure it's in the same folder as this script.")
    exit()

b = cv2.VideoCapture(0)
if not b.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.\n")

while True:
    c, d = b.read()  # c = success flag, d = frame
    if not c:
        print("Failed to capture image.")
        break

    e = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

    f = a.detectMultiScale(
        e,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # draw rectangles on detected faces
    for (x, y, w, h) in f:
        cv2.rectangle(d, (x, y), (x + w, y + h), (255, 0, 0), 4)

    # show the frame OUTSIDE the loop
    cv2.imshow("Face Detection", d)

    # key check outside loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

b.release()
cv2.destroyAllWindows()
