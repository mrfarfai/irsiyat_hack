import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import mysql.connector
from time import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))

db = {}
settings = {}

with open("config.txt") as f:
	for i in f.readlines():
		i = i.split()
		db.update({i[0]: int(i[-1]) if i[-1].isdigit() else i[-1].replace("'", '')})

with open("settings.txt") as f:
	for i in f.readlines():
		i = i.split()
		settings.update({i[0]: int(i[-1]) if i[-1].isdigit() else i[-1].replace("'", '')})

mydb = mysql.connector.connect(host = db["host"], user = db["user"], passwd = db["pass"], database = db["name"])
mycursor = mydb.cursor()

Names = eval(open('Names.txt').read())
encodeListKnown = eval(open('encodeListKnown.txt').read())
 
cap = cv2.VideoCapture(settings["camera"])

name = ""
while True:
	success, img = cap.read()
	imgS = cv2.resize(img,(0,0),None,0.25,0.25)
	imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
	 
	facesCurFrame = face_recognition.face_locations(imgS)
	encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
	
	for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
		matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
		faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)

		matchIndex = np.argmin(faceDis)

		if faceDis[matchIndex] < float(settings["faceDis"]):
		    name = Names[matchIndex]

		else: 
			name = 'Unknown'

		y1,x2,y2,x1 = faceLoc
		y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
		cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
		cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
		cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
	
	if name:
		print(name)
		break

	cv2.imshow('Webcam',img)
	cv2.waitKey(1)