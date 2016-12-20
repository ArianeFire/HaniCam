import cv2
import cv


cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
tab = ["Fadellah1", "Fadellah2", "Fadellah3", "Fadellah4", "Fadellah5", "Fadellah6", "Fadellah7", "Fadellah8", "Fadellah9", "Fadellah10"]

def TAKE_TOF(dirnum) :
   video_capture = cv2.VideoCapture(0)
   print 'Click on S to Take Tof....'
   i=0
   while True:
       # Capture frame-by-frame
       ret, frame = video_capture.read()  

       #PERFORMED DETECTION
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = faceCascade.detectMultiScale(
           gray,
           scaleFactor=1.1,
           minNeighbors=5,
           minSize=(80, 100),
           flags=cv2.cv.CV_HAAR_SCALE_IMAGE
       )
     
       #DRAW RECTANGLE ON FACES   
       for (x, y, w, h) in faces:
           cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
       #On "S" Click Save Frame, Resize it and Save It Again
       key = cv.WaitKey (1)
       if key in [1048691 , ord("s"), "s"]:
          #Save Frame
          cv2.imwrite('tmp/visage1.bmp', frame)  
          if len(faces) > 0 :
             for (x, y, w, h) in faces:
                 img = cv.LoadImage('tmp/visage1.bmp')
    	         image = cv.GetSubRect(img, (x + 20, y + 20, w - 30, h - 30))
    	         cv.SaveImage("tmp/visage.bmp", image)
             #Resize image
             org_img = cv2.imread('tmp/visage.bmp')
             res_img = cv2.resize(org_img, (80, 100), interpolation = cv2.INTER_CUBIC)
             cv2.imwrite("faces/s"+str(dirnum)+"/"+tab[i]+".bmp", res_img) #cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)
             if i >= len(tab) -1 :
                break
             i = i + 1

       # Display the resulting frame
       cv2.imshow('Video', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
          break

   # When everything is done, release the capture
   video_capture.release()
   cv2.destroyAllWindows()

   print "Toutes les photos sont prises ..."
num = input('Saisir le numero de Dossier')
TAKE_TOF(num);

