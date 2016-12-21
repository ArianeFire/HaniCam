# HANICAM

HaniCam is IOT (Internet of Things) project for handling student absence at school using Facial Recognition.

Indeed Hanicam is composed of two system, an embedded system provided with Camera used to perform facial recognition in the classroom 
to determine absent student; In other side, we have an responsive web application used by teacher to launch and stop recognition in 
the classroom and to handle absence list as well.

### Embedded System :

Embedded System is intergrated in a Raspberry PI, it use a Pythons FrameWork to perform facial recognition and also NodeJs server with
mongodb NoSql database. This server will handle student list (insert new student, increment number of absence or create an new teacher).

### Web Application

It is the Front-End of the NodeJs Server developped in the Embedded System. It allow student to launch & stop facial recognition
and also teacher can use it to handle list of student absence.

### Run this Project (Linux Machine Only).

1- Download the project.</br>
2- In order to run this project, you will need to install OpenCV 3.0 and NodeJs.</br>
3- You should also install properly this framework (it's necessary for Facial recognition) [See GitHub Repo](https://github.com/bytefish/facerec)<br/>
4- Finally launch NodeJs Server in the "HanCamV2" folder (with node app.js")<br/>
   The app is accessible from "localhost:8000". For authentification purpose use (email : tbouchentouf@gmail.com & pass : toumi).
   From that app you will be able to launch Facial Recognition. 
   (Before, you need to create your images Database using "taker.py" in "HanCamV2" folder).


