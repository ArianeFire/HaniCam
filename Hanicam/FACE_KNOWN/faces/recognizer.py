import cv2
import cv
import face


#Function deleting the path link
def deleteLink(link):
    lien = str(link)
    lien = lien.replace('/home/seydou/Hanicam/FACE_KNOWN/faces/','')
    lien = lien.replace('.bmp','')
    
    #Suppression des indices des noms
    for i in range(0,11) :
        lien = lien.replace(str(i), "")
        
    return lien

#Function writing the lists of students in txt file
def writeInFile(listes):
    fichier = open('/opt/lampp/htdocs/www/Hancam/ressources/liste.txt', 'w')
    #for line in listes :
    fichier.write(listes)
    fichier.close();

#Function Allowing Script to start
def allowScript() :
    fichier1 = open("script/info.txt", "w");
    fichier1.write("oui"+"\n");
    fichier1.write("oui");
    fichier1.close();



#STARTING REGNITION
cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
listes = []
listes_set = set(listes)
nb_p = 2
path = "/home/seydou/Hanicam/FACE_KNOWN/s"
distances = []
results = []
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
            collections = []
            for i in range(0,2) :
            	collections.add(face.Collection(path+str(i)))
            visage = face.Tableau('detect/visage_res.bmp')
            for collection in collections :
            	rets = collection.reconnaitre(visage)
            	resultats.add(rets)
            	distances.add(rets[0])
            indice = min(distances)
            rets = resultats[indice]
            print "Dsitance : ", rets[0]
            if rets[1] != None :
               print "Lien : ", rets[1].getLien()
               nom = deleteLink(rets[1].getLien())
               if nom not in listes_set :
               	writeInFile(nom)
               	listes_set.add(nom)
               
               
               

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        #allowScript()
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

