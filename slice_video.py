import cv2
import os

curdir = "C:/202105_lab/02.git/yolov5/data/videos"
video_path = cv2=cv2.VideoCapture(os.path.join(curdir, "dog_sample.mp4"))

cnt = 0

while video_path.isOpened():
    ret, image = video_path.read() 
    image = cv2.resize(image, (412, 412)) 
    if int(video_path.get(1)) % 10 == 0: 
        cv2.imwrite(os.path.join(os.path.curdir, 'capture', '%d.png' % video_path.get(1)), image) 
        print("Frame Captured: %d" % video_path.get(1)) 
        cnt += 1
    print(2)
print(1)
        
video_path.release()
