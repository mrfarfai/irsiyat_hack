
for root, dirs, files in os.walk('../img'):
	for file in files:
		path = root.replace("\\", "/")
		curImg = cv2.imread(f'{root}/{file}')
		images.append(curImg)
		name = path.split("/")
		if name[2] == "student":
			name[3] = name[4]
		encodes.append(f'{name[2]}_{name[3]}')

def findEncodings(images):
	encodeList = []
	k = 1
	for img in images:
		print(k)
		k = k + 1
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		encode = face_recognition.face_encodings(img)[0]
		encodeList.append(encode)
	return encodeList
	 
	 
encodeListKnown = findEncodings(images)
print(encodes)
for e in encodeListKnown:
	print(e,"\n")