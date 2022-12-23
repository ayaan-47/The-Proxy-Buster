import cv2
#face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap  = cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(grayscale, 1.3 ,5)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 250), 2)
    cv2.imshow('Detected Face Image',  img)

   
    if cv2.waitKey(1) & 0xff == ord(' '):
        break

cap.release()

cv2.destroyAllWindows()




