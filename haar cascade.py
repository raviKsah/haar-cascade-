# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 16:08:54 2018

@author: hp
"""

import cv2 


stop_cascade = cv2.CascadeClassifier('stop_sign_pjy.xml')
traffic_cascade = cv2.CascadeClassifier('traffic_light.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stopsigns = stop_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in stopsigns:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        print('found stop sign')
    traffics = traffic_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in traffics:
          cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
          roi_gray = gray[ey:ey+eh, ex:ex+ew]
          roi_color = img[ey:ey+eh, ex:ex+ew]
          print('found traffic light')

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()