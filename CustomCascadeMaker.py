import cv2
import os
import time
 
#####################################################
 
myPath = r'C:\Users\ayylmbo\Desktop\Custom Gestures Project\customImages\\' # Rasbperry Pi:  '/home/pi/Desktop/data/images'
cameraNo = 0
cameraBrightness = 0
moduleVal = 10  # SAVE EVERY iTH FRAME TO AVOID REPETITION
minBlur = 10  # SMALLER VALUE MEANS MORE BLURRINESS PRESENT
grayImage = False # IMAGES SAVED COLORED OR GRAY
saveData = True   # SAVE DATA FLAG
showImage = True  # IMAGE DISPLAY FLAG
imgWidth = 640
imgHeight = 480
 
 
#####################################################
 
global countFolder
cap = cv2.VideoCapture(cameraNo)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,cameraBrightness)
 
 
count = 0
countSave =0
 
def saveDataFunc():
    global countFolder
    countFolder = 0
    while os.path.exists( myPath+ str(countFolder)):
        countFolder += 1
    os.makedirs(myPath + str(countFolder))
 
if saveData:saveDataFunc()
 
 
while True:
    success, img = cap.read()
    img = cv2.resize(img,(imgWidth,imgHeight))
    if grayImage:img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if saveData:
        blur = cv2.Laplacian(img, cv2.CV_64F).var()
        if count % moduleVal ==0 and blur > minBlur:
            #imgBlur = cv2.GaussianBlur(img,(7,7),0) do this to blur the image if its too sharp from a video perspective
            nowTime = time.time()
            cv2.imwrite(myPath + str(countFolder) +
                    '/' + str(countSave)+"_"+ str(int(blur))+"_"+str(nowTime)+".png", img) #change img to imgBlur
            countSave+=1
            #print("saved")
            #print(myPath + str(countFolder) +'/' + str(countSave)+"_"+ str(int(blur))+"_"+str(nowTime)+".png", img)
        count += 1
 
    if showImage:
        cv2.imshow("Image", img)
 
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()