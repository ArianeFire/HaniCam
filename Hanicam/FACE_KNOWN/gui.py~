#!/usr/bin/envpython2
# -*-coding:utf-8-*-
import cv
import cv2
import time
import os
import sys
import face
import numpy as np


#(281, 191, 80, 100)

if __name__  == "__main__":
   #Ce code ne s’e x c u t e que si on e x c u t e directement le module(pas en cas d’import)
   webcam = cv.CaptureFromCAM (0)
   #nb_tof = input("Saisir nombre de photos à prendre :")
   
   #i = 0
   tab = ["Seydou", "Seydou1", "Seydou2",  "Yassir", "Yassir1","Yassir2", "RHOR", "RHOR1", "RHOR2", "Telephone",  "Telephone1"]
   #tab = ["SeydouOne", "SeydouTwo", "SeydouThree", "SeydouFour", "SeydouFive", "SeydouSix", "SeydouSeven", "SeydouEight", "SeydouNine"]
   #print "Appuyez sur S pour prendre la photo"
   #while True:
   #   image = cv.GetSubRect(cv.QueryFrame(webcam), (281, 191, 80, 100))
   #   cv.ShowImage("webcam", image)
   #   key = cv.WaitKey (1)
      #La touche pour prendre la photo est la touche s
      #Sous le linux u t i l i s pour tester,la valeur correspondante
      #tait 1048691.
      #Sous Windows, la valeur tait ord("s"),soit 115.
      #Sous certaines machine, cette valeur peut tre "s".
   #   if key in [1048691 , ord("s"), "s"]:
   #      cv.SaveImage("faces/"+tab[i]+".bmp", image)
   #      if i >= len(tab) -1 :
   #         break
   #      i = i + 1
   #print "Toutes les photos sont prises ..."
   
   input('Appuyer sur O pour la reconnaissance')
   #Reconnaissance

   #collection = face.Collection();
   #fichier = open("files/liste.txt","a");
   cascPath = "youtube/haarcascade_frontalface_default.xml"
   faceCascade = cv2.CascadeClassifier(cascPath)
   while True:
      image = cv.GetSubRect(cv.QueryFrame(webcam), (281, 191, 80, 100))
      cv.ShowImage("webcam", image)
      cv.SaveImage("detect/visage.bmp", image)
      img = cv2.imread('detect/visage.bmp')
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80, 100),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
      )

      key = cv.WaitKey (1)
      
      visage = face.Tableau('detect/visage.bmp')
      collection = face.Collection();
      rets = collection.reconnaitre(visage)
      #if rets[1] != None :
         #print rets[1].getLien()
         #print rets[0]
         #fichier.write(rets[1]+"\n");
         #fichier1 = open("script/info.txt", "w");
         #fichier1.write("oui"+"\n");
         #fichier1.write("oui");
         #fichier1.close();
      #time.sleep(1)
      print rets[0]
      print "NBRE : ",str(len(faces))
   #fichier.close();
   
