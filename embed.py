###A simple implimentation of OpenCv (cv2 libraries) for Face Recognisation by user input data set of picture #######

# this project have two py file one is embed for taking dat input and another is recg for recognisation of face fromj availbe data set########

#some basic Libraries to be imported to run this project are as below
import cv2 
import face_recognition
import pickle
name=input("Enter Name :")
ref_id=input("Enter unique id :")

try:
	f=open("ref_name.pkl","rb")

	ref_dictt=pickle.load(f)
	f.close()
except:
	ref_dictt={}
ref_dictt[ref_id]=name

f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f)
f.close()

try:
	f=open("ref_embed.pkl","rb")

	embed_dictt=pickle.load(f)
	f.close()
except:
	embed_dictt={}

print("Type (s) to click picture for 4 times")
print("or Type (q) to quit the proccess")

for i in range(4):
	key = cv2. waitKey(1)
	webcam = cv2.VideoCapture(0) # change ur webcam id , if you are using external cam plse (1) instead of 0;
	while True:
	     
		check, frame = webcam.read()

		cv2.imshow("Capturing", frame)
		small_frame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)
		rgb_small_frame = small_frame[:, :, ::-1]
		
		key = cv2.waitKey(1)

		if key == ord('s') : 
			face_locations = face_recognition.face_locations(rgb_small_frame)
			if face_locations != []:


				face_encoding = face_recognition.face_encodings(frame)[0]
				if ref_id in embed_dictt:
					embed_dictt[ref_id]+=[face_encoding]
				else:
					embed_dictt[ref_id]=[face_encoding]
				webcam.release()

				cv2.waitKey(1)
				cv2.destroyAllWindows()     
				break
		elif key == ord('q'):
			print("Turning off camera.")
			webcam.release()
			print("Camera off.")
			print("Program ended.")
			cv2.destroyAllWindows()
			break
f=open("ref_embed.pkl","wb")
pickle.dump(embed_dictt,f)
f.close()
