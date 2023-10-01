import os
import cv2
import numpy as np
import faceRecognition as fr
import keylogger
import sys


#This module captures images via webcam and performs face recognition
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')#Load saved training data

name = {0 : "sailesh",1 : "Dhanush",2:"BHARATH"}

cap = cv2.VideoCapture(0)

while True:
    ret,test_img=cap.read()# captures frame and returns boolean value and captured image
    faces_detected,gray_img=fr.faceDetection(test_img)



    for (x,y,w,h) in faces_detected:
      cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=7)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    cv2.waitKey(10)


    for face in faces_detected:
        (x,y,w,h)=face
        roi_gray=gray_img[y:y+w, x:x+h]
        label,confidence=face_recognizer.predict(roi_gray)#predicting the label of given image
        print("confidence:",confidence)
        print("label:",label)
        fr.draw_rect(test_img,face)
        predicted_name=name[label]
        if confidence < 60:#If confidence less than 37 then don't print predicted face text on screen
           fr.put_text(test_img,predicted_name,x,y)
           if predicted_name=="BHARATH":
               print("WELCOME DEVIL")
               resized_img = cv2.resize(test_img, (1000, 700))
               cv2.imshow('face recognition tutorial ',resized_img)
               cap.release()
               cv2.destroyAllWindows()
               sys.exit()
        else:
            print("INVALID USER")
            exec(open("keylogger.pyw").read())
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()
