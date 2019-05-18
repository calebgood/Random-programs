import numpy as np
import cv2

cap = cv2.VideoCapture("traffic-mini.mp4")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cv2.imshow('Epic', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


'''
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGR) # for converting to black&white
    
    # Display the resulting frame
    cv2.imshow('frame',gray)'''
