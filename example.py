from vlcplayer import Player
import time
import cv2

if "__main__" == __name__:
    n = 0
    allow = 0
    c1 = Player()
    #c2 = Player()
    #c3 = Player()
    #c4 = Player()
    c1.play("C:/Users/zang/Desktop/AI for Video V3.0/video/video_test/test_video1.mp4",1)
    #c2.play("rtsp://172.16.9.121:554/snl/live/1/1",2)
    #c4.play("rtsp://172.16.9.122:554/snl/live/1/1",3)
    #c4.play("rtsp://172.16.9.117:554/snl/live/1/1",4)
    while True:
        frame = c1.image_get(1)
        if len(frame) != 1:
            cv2.imshow('image1',frame)
            cv2.waitKey(10)
