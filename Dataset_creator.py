import cv2
import numpy as np
import pyautogui
import os
face_cascade = cv2.CascadeClassifier(r'D:\Jithu Pgm working\Jithu\Vishva_programs\OPENCV_PLAY\XML\haarcascade_frontalface_default.xml')

presenting=int(input("Are you for live or video?! If video press 1 else press 2 for live: "))
if(presenting==1):
	enter_the_path=input("Enter the path of the videofile: ").strip()
	cap = cv2.VideoCapture(f"{enter_the_path}")
else:
	cap = cv2.VideoCapture(0)


name=input("Enter the name: ").strip()
confirmation=input("Is he a terrorist?!\nEnter yes or no:")
if(confirmation.lower()=='yes'):
	terrorist=True
else:
	terrorist=False

if(terrorist):
	flag=1
	while(flag):
		newpath = r'D:\Jithu Pgm working\Jithu\Vishva_programs\OPENCV_PLAY\New folder\face-recognition-using-deep-learning-master\dataset\Terrorist' 
		newpath+=f"\Terrorist_{name}"		
		if not os.path.exists(newpath):
			os.makedirs(newpath)
			flag=0
		else:
			name=input("Enter the name properly as a name already exisiting like that: ").strip()
else:
	identity=input("Enter the id number:").strip()
	flag=1
	while(flag):
		newpath = r'D:\Jithu Pgm working\Jithu\Vishva_programs\OPENCV_PLAY\New folder\face-recognition-using-deep-learning-master\dataset\Our Batch'
		newpath+=f"\{identity}_{name}"
		print(newpath)
		if not os.path.exists(newpath):
			os.makedirs(newpath)
			flag=0
		else:
			name=input("Enter the name properly as a name already exisiting like that: ").strip()
			identity=input("Enter the id number:").strip()

#D:\Jithu Pgm working\Jithu\Vishva_programs\OPENCV_PLAY\New folder\face-recognition-using-deep-learning-master\videoplayback.mp4

k=0
while(1):
    
    return_value, img =cap.read()
    val=str(k).zfill(5)
	
    cv2.imwrite((f"{newpath}\{val}.png"),img)
    k+=1

    cv2.imshow('Face_eye',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break  
cap.release()
cv2.destroyAllWindows()    

