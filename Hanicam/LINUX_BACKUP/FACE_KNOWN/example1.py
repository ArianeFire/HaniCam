import cv2
import cv
import face


cascPath = "youtube/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

def TAKE_TOF() :
   tab = ["YASSIR1", "YASSIR2", "YASSIR3", "YASSIR4", "YASSIR5", "YASSIR6", "YASSIR7", "YASSIR8", "YASSIR9", "YASSIR10"]
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
             cv2.imwrite("faces/"+tab[i]+".bmp", res_img) #cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)
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



#Function deleting the path link
def deleteLink(link):
    lien = str(link)
    lien = lien.replace('/home/ariane/FaceKnown/faces/','')
    lien = lien.replace('.bmp','')
    
    #Suppression des indices des noms
    for i in range(0,11) :
        lien = lien.replace(str(i), "")
        
    return lien

#Function writing the lists of students in txt file
def writeInFile(listes):
    fichier = open('/var/www/html/liste.txt', 'w')
    for line in listes :
        fichier.write(line+"\n")
    fichier.close();

#Function Allowing Script to start
def allowScript() :
    fichier1 = open("script/info.txt", "w");
    fichier1.write("oui"+"\n");
    fichier1.write("oui");
    fichier1.close();


#TAKE_TOF()
#input('Taper 0 pour commencer la reconnaissance')

#STARTING REGNITION
video_capture = cv2.VideoCapture(0)
listes = []
listes_set = set(listes)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    
    #Save Frame
    cv2.imwrite('detect/visage1.bmp', frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 100),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
        
    #for (x, y, w, h) in faces:
    #        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Draw a rectangle around the faces
    if len(faces) > 0 :
    	for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            img = cv.LoadImage('detect/visage1.bmp')
    	    image = cv.GetSubRect(img, (x + 20, y + 20, w - 30, h-30))
    	    cv.SaveImage("detect/visage.bmp", image)
            
            #Resize image
            org_img = cv2.imread('detect/visage.bmp')
            res_img = cv2.resize(org_img, (80, 100), interpolation = cv2.INTER_CUBIC)
            cv2.imwrite('detect/visage_res.bmp', res_img)  #cv2.cvtColor(res_img, cv2.COLOR_BGR2GRAY)
            #Perform Recognition 
            collection = face.Collection()
            visage = face.Tableau('detect/visage_res.bmp')
            rets = collection.reconnaitre(visage)
            print "Dsitance : ", rets[0]
            if rets[1] != None :
               print "Lien : ", rets[1].getLien()
               listes_set.add(deleteLink(rets[1].getLien()))
               
               

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        writeInFile(listes_set)
        allowScript()
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

