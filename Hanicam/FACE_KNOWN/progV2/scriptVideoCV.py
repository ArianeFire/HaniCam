from facerec.feature import Fisherfaces
from facerec.classifier import NearestNeighbor
from facerec.model import PredictableModel
from PIL import Image
import numpy as np
from PIL import Image
import sys, os
#sys.path.append("../..")
import cv2
import multiprocessing



model = PredictableModel(Fisherfaces(), NearestNeighbor())
vc=cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mapping = {'s1': 'Seydou', 's2':'oussama', 's3':'mahi'}
listes = set([])
def writeInFile(listes):
    fichier = open('../../../HancamV2/ressources/liste.txt', 'w')
    #for line in listes :
    fichier.write(listes)
    fichier.close();

#Lecteur du dossier image
def read_images(path, sz=(256,256)):
    """Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes 

    Returns:
        A list [X,y]

            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
    """
    c = 0
    X,y = [], []
    folder_names = []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            folder_names.append(subdirname)
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    # resize to given size (if given)
                    if (sz is not None):
                        im = cv2.resize(im, sz)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c = c+1
    return [X,y,folder_names]



pathdir='data/gi4'
#Premiere phase de la reconnaissance

[X,y,subject_names] = read_images(pathdir)
list_of_labels = list(xrange(max(y)+1))

subject_dictionary = dict(zip(list_of_labels, subject_names))
model.compute(X,y)

#Boucle principale effectuant la reconnaissance
while (1):
    rval, frame = vc.read()
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 3)

    for (x,y,w,h) in faces:
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        sampleImage = gray[y:y+h, x:x+w]
        sampleImage = cv2.resize(sampleImage, (256,256))

        #capiamo di chi e sta faccia
        [ predicted_label, generic_classifier_output] = model.predict(sampleImage)
        print [ predicted_label, generic_classifier_output]
        #scelta la soglia a 700. soglia maggiore di 700, accuratezza minore e v.v.
        if int(generic_classifier_output['distances']) <=  700:
        		nom = mapping[str(subject_dictionary[predicted_label])]
        		cv2.putText(img,'Tu es : '+nom, (x,y), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,250),3,1)
        		if nom not in listes :
        		   writeInFile(nom)
        		   listes.add(nom)
        		
    cv2.imshow('result',img)
    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()
vc.release()


