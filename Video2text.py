import cv2
import math
import os
import settings
import time
from numba import jit
@jit
def play():
    dic = settings.char_coll
    dic.reverse()
    video = cv2.VideoCapture(settings.video_path)
    opened = video.isOpened()
    out_wid = settings.out_width
    out_hei = settings.out_height
    frame_time = 1 / video.get(cv2.CAP_PROP_FPS)
    clock = time.time()
    first = True
    buffer = None
    same_count = 0
    while(opened):
        opened, frame = video.read()
        if(opened == False):
            break
        if((frame == buffer).all()):
            same_count += 1
            continue
        else:
            buffer = frame
        s_frame = cv2.resize(frame, (int(out_wid), int(out_hei)), cv2.INTER_CUBIC)
        sg_frame = cv2.cvtColor(s_frame,cv2.COLOR_RGB2GRAY)
        s = ''
        for i in range(len(sg_frame)):
            for j in range(len(sg_frame[0])):
                index = math.floor(sg_frame[i][j] * len(dic) / 256)
                s += dic[index]
        t = time.time()
        while(clock + frame_time * (same_count + 1) - 0.0027 > t):
            t = time.time()
        if(first):
            try:
                os.system(settings.audio_path)
                first = False
            except:
                first = False
        print(s)
        clock = time.time()

if __name__ == "__main__":
    play()
            


            

                 
            