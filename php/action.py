import os
import sys
import cv2
import numpy as np
import face_recognition

os.chdir(os.path.dirname(os.path.abspath(__file__)))
names = eval(open('Names.txt').read())
encodeListKnown = eval(open('encodeListKnown.txt').read())

uid = sys.argv[1]
curImg = cv2.imread("../templets/img/user/" + uid + ".png")
facesCurFrame = face_recognition.face_locations(curImg)
names.append(uid)
curImg = cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
encodeListKnown.append(face_recognition.face_encodings(curImg)[0])

open('Names.txt', 'w').write(str(names))
encodeListKnown = str(encodeListKnown)
encodeListKnown = encodeListKnown.replace("array(", "")
encodeListKnown = encodeListKnown.replace(")", "")
open('encodeListKnown.txt', 'w').write(str(encodeListKnown))