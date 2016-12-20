#!/usr/bin/envpython2
#-*-coding:utf-8 -*-
import cv
import math
import numbers
import numpy as np
import os
import sys
import time

def list_de_iplimage(image):
    "Renvoie la forme liste d’une image OpenCV"
    return [[cv.Get2D(image , i, j)[0] for j in xrange(image.width )]
                                       for i in xrange(image.height )]
class Tableau:
    def __add__(self , autre):
        "Additionne avec un Tableau ou un scalaire"
        if isinstance(autre , Tableau ): 
           return Tableau(self.tab + autre.tab)
        elif isinstance(autre , numbers.Number ):
           return Tableau(self.tab + autre)
        else :
           raise TypeError("Tableau.__add__ : Tableau ou scalaire attendu")

    def __div__(self , autre):
        "Divise par un scalaire"
        return Tableau(self.tab / autre)
    def __getitem__(self , index ):
        "Renvoie un coefficient du Tableau , pour pouvoir utiliser tableau[index]"
        if isinstance(index , int) and self.largeur  != 1:
          return Tableau(self.tab[index ])
        else :
          return self.tab[index]

    def __init__(self , source , nom=str(time.time ())):
       """Constructeur d’un objet Tableau2 On peut lui passer :
       *une c h a  n e de c a r a c t r e , qui sera le chemin de l’ image charger Tableau
       *une image au format OpenCV passer en Tableau
       *un array numpy passer en Tableau """
       if isinstance(source , str):
          self.tab = np.array(list_de_iplimage(cv.LoadImage(source , cv.CV_LOAD_IMAGE_GRAYSCALE )))
       elif isinstance(source , cv.iplimage ):
          self.tab = nb.array(list_de_iplimage(source ))
       elif isinstance(source , (np.ndarray , list )):
          self.tab = np.array(source)
       else :
          raise TypeError("Tableau.__init__ : %s inattendu" % type(source ))
       self.nom = nom
       self.calc_dimensions ()
       self.lien = source

    def getLien(self) :
        return self.lien

    def __len__(self):
       "Pour pouvoir utiliser len(tableau) au cas  o  "
       return len(self.tab)

    def __mul__(self , autre , element_par_element=False ):
       """ Multiplie : multiplication de matrice , ou par un scalaire Le flag element_par_element indique,
        s’il est vrai, qu'on n’utilise pas la multiplication de l’a l g b r e desmatrices,mais une multiplication
        element par element de deux matrices de memes dimensions
       """
       if isinstance(autre , Tableau):
          if element_par_element:
             return Tableau(self.tab * autre.tab)
          else :
             resultat = np.dot(self.tab , autre.tab)
             if isinstance(resultat , numbers.Number ):
                return resultat
             else :
               return Tableau(resultat)
       elif isinstance(autre , numbers.Number ):
            return Tableau(self * autre)
       else :
            raise TypeError("Tableau.__mul__ : Tableau ou scalaire attendu")

    def __setitem__(self , index , valeur ):
      """Modifie un coefficient du Tableau :
      i m p l m e n t e tableau[index]=valeur """
      self.tab[index] = valeur

    def __sub__(self , autre):
      "Additionne avec un Tableau ou un scalaire"
      if isinstance(autre , Tableau ):
          return Tableau(self.tab - autre.tab)
      elif isinstance(autre , numbers.Number ): 
          return Tableau(self.tab - autre)
      else :
          raise TypeError("Tableau.__sub__ : Tableau ou scalaire attendu")

    def afficher(self , nom=None):
       """Affiche le Tableau,comme une image, dans une f e n t r e
          Utilise OpenCV pour cela 
       """
       if nom is None:
          nom = self.nom
          cv.ShowImage(nom , self.vers_iplimage ())

    def calc_dimensions(self):
       "Calcule les dimensions du Tableau"
       self.hauteur = len(self.tab)
       try :
           self.largeur = len(self.tab [0])
       except TypeError:
           self.largeur = 1

    def calc_elements_propres(self):
       "Calcule valeurs propres et vecteurs propres du tableau"
       valeurs , vecteurs = np.linalg.eig(self.tab)
       self.val_propres = list(valeurs)
       self.vect_propres = [Tableau(vect) for vect in vecteurs]

    def covariance(self):
       "Renvoie le Tableau de covariance du Tableau"
       return self * self.transposee ()

    def dimensions(self):
       "Renvoie les dimensions - hauteur * largeur - du tableau"
       return self.hauteur , self.largeur
    def en_colonne(self):
       "Renvoie le Tableau comme un vecteur colonne"
       return self.redimensionnee (-1)

    def inverse(self):
       "Renvoie l’inverse du Tableau dans l’ a g  b r e  des matrices"
       return Tableau(np.linalg.inv(self.tab))

    def mahalanobis(self , autre , cov):
       "Calcule la distance de Mahalanobis entre deux Tableaux"
       a = (self - autre) * cov.inverse () * (self - autre)
       if a < 0 :
          return 10000
       return math.sqrt(a)

    def mettre_en_colonne(self):
       "Met le Tableau en forme de vecteur colonne"
       self.redimensionner (-1)

    def redimensionnee(self , nouvelle_forme ):
       """Renvoie le Tableau sous une nouvelle forme
        Le nombre total d’ lments doit rester le m  m e """
       tab = Tableau(np.reshape(self.tab , nouvelle_forme ))
       tab.calc_dimensions ()
       return tab

    def redimensionner(self , nouvelle_forme ):
       """Change la forme du Tableau
       Le nombre total d’lments reste le m  m e"""
       self.tab = np.reshape(self.tab , nouvelle_forme)
       self.calc_dimensions ()

    def transposee(self):
       "Renvoie la  t r a n s p o s e  du Tableau"
       return Tableau(np.transpose(self.tab))

    def transposer(self):
       "Transpose le Tableau"
       self.tab   = np.transpose(self.tab)

    def vers_iplimage(self , profondeur=cv.IPL_DEPTH_8U ):
       "Renvoie l’iplimage   quivalente   (format OpenCV)"
       temp = cv.CreateImage ((self.largeur , self.hauteur), cv.IPL_DEPTH_64F , 1)
       for (i, ligne) in enumerate(self.tab):
           for (j, valeur) in enumerate(ligne):
               cv.Set2D(temp , i, j, valeur)
               img = cv.CreateImage ((self.largeur , self.hauteur), profondeur , 1)
               cv.Convert(temp , img)
       return img

class Collection:

    def __init__(self , chemin="/home/ariane/FaceKnown/faces/"):
       "Constructeur d’un objet Collection"
       self.liste_faces = [Tableau(chemin + fichier) for fichier in os.listdir(chemin)]
           
       self.nb_faces = len(self.liste_faces)
       # On prepare la Collection pour lareconnaissance "
       self.calc_moyenne ()
       self.calc_ecarts ()
       self.calc_covariance ()
       self.calc_faces_propres ()
       self.calc_coeff_faces ()

    def calc_covariance(self):
       "Calcule la covariance des faces  n o r m a l i s e s  de la Collection"
       self.covariance = self.ecarts.transposee (). covariance ()

    def calc_moyenne(self):
       "Calcule la moyenne des faces de la Collection"
       self.moyenne = reduce(Tableau.__add__ , self.liste_faces) / self.nb_faces

    def calc_coeff_faces(self):
       """Calcule les coefficients des faces de la collection,
          dans la base des faces propres
       """
       self.coeff_faces = Tableau ([self.coeff(face)  for face in self.ecarts.transposee()])
       self.covar_coeff = self.coeff_faces.transposee().covariance()

    def calc_ecarts(self):
       "Calcule le Tableau des carts la moyenne"
       self.ecarts = Tableau([(face - self.moyenne).en_colonne().tab for face in self.liste_faces ]).transposee()
  
    def calc_faces_propres(self):
       "Calcule les faces propres de la collection"
       self.covariance.calc_elements_propres ()
       self.faces_propres = [self.ecarts * vect for vect in self.covariance.vect_propres]
       # Pour un affichage, redimensionner en (100,80)

    def coeff(self , tableau):
       "Renvoie les coefficients d’un tableau sur la base des faces propres"
       return [face * tableau.en_colonne () for face in self.faces_propres]

    def reconnaitre(self , image):
       """ Reconnait ou non une image.
        Sauvegarde la face connue la plus proche dans le fichier resultat.bmp,
        et renvoie la distance entre le visage r e c o n n a t r e et cette face """
       coeff = Tableau(self.coeff(image  - self.moyenne ))
       distances = [coeff.mahalanobis(coeff_face , self.covar_coeff) for coeff_face in self.coeff_faces]
       distance_min = min(distances)
       i = distances.index(distance_min)
       cv.SaveImage("resultatTMP.bmp", self.liste_faces[i].vers_iplimage ())
       if distance_min <= 1.0 :
          cv.SaveImage("resultat.bmp", self.liste_faces[i].vers_iplimage ())
          return [distance_min, self.liste_faces[i]]
       return [distance_min, None]


