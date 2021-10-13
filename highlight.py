import numpy as np
import cv2
import json

# def section():
#     with open("log/dog_vidio-1.json", "r") as f:
#         json_data = json.load(f)
#     print(json.dumps(json_data))






def Highlight(path):
    result_path='data/result/frame.mp4'

    codec=cv2.VideoWriter_fourcc(*'MP4V')
    cap = cv2.VideoCapture(path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))

    vid_writer = cv2.VideoWriter(result_path, codec, fps, size)
    frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    print('총 Frame 갯수:', frame_cnt, 'FPS:', round(fps), 'Frame 크기:', size)

    print(path)
    

    while(cap.isOpened()):
        ret, image = cap.read()
        # cv2.imshow(path, image) # 동영상 확인용
        # cv2.waitKey(delay)
            
        if cap.get(1) > 100 and cap.get(1) < 200:
 
            vid_writer.write(image)
        
        if not ret: # 동영상 끝나면 닫겠다.
            print(cap.get(1), type(cap.get(1)))
            break

    # cap.release() # 동영상확인후 닫는용도
    # cv2.destroyAllWindows()


if __name__ == '__main__':
	Highlight('data/videos/dog_sample.mp4')
    # section()