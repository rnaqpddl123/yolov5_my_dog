import numpy as np
import cv2
import json
import argparse
import os
from pathlib import Path

from json_move import move_dog
from utils.general import create_dir


import torch

@torch.no_grad()
def Highlight(path,
            result_name,
            json_name,
            json_dir
            ):
    Highlight = "../Frontend-main/webapp/static/runs/highlight"
    
    create_dir(Highlight)
    
    HL_frame = move_dog(json_name,json_dir)

    for i in range(len(HL_frame)):
        try:
            # mp4파일일경우
            codec=cv2.VideoWriter_fourcc(*'MP4V')
        except:
            # avi파일일 경우
            codec=cv2.VideoWriter_fourcc(*'FMP4')

        cap = cv2.VideoCapture(path)
        fps = cap.get(cv2.CAP_PROP_FPS)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        size = (int(width), int(height))

        # vid_writer = cv2.VideoWriter(result_path, codec, fps, size)
        frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        print('총 Frame 갯수:', frame_cnt, 'FPS:', round(fps), 'Frame 크기:', size)
            
        result_name = os.path.splitext(result_name)[0]
        result_path = f"{Highlight}/{result_name}_{i}.mp4"
        
        # 해당 코덱을 사용하기위해서 https://github.com/cisco/openh264/releases 맞는 버전을 확인해서 C:\Users\Playdata\Anaconda3에 집어넣었다
        codec_writer = cv2.VideoWriter_fourcc(*'avc1')
        vid_writer = cv2.VideoWriter(result_path, codec_writer, fps, size)


        while(cap.isOpened()):
            ret, image = cap.read()
            # cv2.imshow(path, image) # 동영상 확인용
            # cv2.waitKey(delay)
            
            if cap.get(1) > (HL_frame[i]*60) and cap.get(1) < (HL_frame[i]*60)+1800:
                
    
                vid_writer.write(image)
            
            if not ret: # 동영상 끝나면 닫겠다.
                print(cap.get(1), type(cap.get(1)), result_path)
                break
