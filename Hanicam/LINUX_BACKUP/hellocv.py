from cv2.cv import *
  
img = LoadImage("/home/ariane/pub.png")
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)
