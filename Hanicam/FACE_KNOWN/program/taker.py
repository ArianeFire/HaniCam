import cv2
import os
import time


vc=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
pathdir='data/gi4'
#inizializzazione:
#quanti = int(raw_input('combien de personnes voulez vous reconnaitre avec votre webcam? \n numero:'))
num = int(raw_input('Numero de dossier : '))
nome = raw_input('Quel est votre nom : ')
print "Appuyer sur S pour commencer la prise ....."
for i in range(0,1):
    if not os.path.exists(pathdir+"/s"+str(num)): os.makedirs(pathdir+"/s"+str(num))
    while (1):
        ret,frame = vc.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 3)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('Recognition',frame)
        
        if cv2.waitKey(10) in [1048691 , ord("s"), "s"]:
            break
    cv2.destroyAllWindows()

    #comincio a scattare
    #start = time.time()
    count = 1
    while count <= 10:
        
        ret,frame = vc.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 3)
        for (x,y,z,h) in faces :
        		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if cv2.waitKey(10) in [1048691 , ord("s"), "s"] :
            if len(faces) > 0 :
        	       for (x,y,w,h) in faces:
                    #cv2.putText(frame,'Click!', (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),3,1)
            		  resized_image = cv2.resize(frame[y:y+h,x:x+w], (273, 273))
            		  cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                	  print  pathdir+nome+str(count)+'.jpg'
                	  cv2.imwrite( pathdir+"/s"+str(num)+"/"+nome+str(count)+'.jpg', resized_image );
                	  count +=1
        cv2.imshow('Recognition',frame)
    cv2.destroyAllWindows()

