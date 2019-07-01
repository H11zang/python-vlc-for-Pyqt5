import os, time
# 设置VLC库路径，需在import vlc之前
os.environ['PYTHON_VLC_MODULE_PATH'] = "./vlc-3.0.7.1"
import vlc
import ctypes
import time
import sys
import cv2
import numpy
from PIL import Image

VIDEOWIDTH = 960
VIDEOHEIGHT = 540
size = VIDEOWIDTH * VIDEOHEIGHT * 4
buf1 = (ctypes.c_ubyte * size)()
buf_p1 = ctypes.cast(buf1, ctypes.c_void_p)
VideoLockCb1 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf2 = (ctypes.c_ubyte * size)()
buf_p2 = ctypes.cast(buf2, ctypes.c_void_p)
VideoLockCb2 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf3 = (ctypes.c_ubyte * size)()
buf_p3 = ctypes.cast(buf3, ctypes.c_void_p)
VideoLockCb3 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf4 = (ctypes.c_ubyte * size)()
buf_p4 = ctypes.cast(buf4, ctypes.c_void_p)
VideoLockCb4 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf5 = (ctypes.c_ubyte * size)()
buf_p5 = ctypes.cast(buf5, ctypes.c_void_p)
VideoLockCb5 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf6 = (ctypes.c_ubyte * size)()
buf_p6 = ctypes.cast(buf6, ctypes.c_void_p)
VideoLockCb6 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf7 = (ctypes.c_ubyte * size)()
buf_p7 = ctypes.cast(buf7, ctypes.c_void_p)
VideoLockCb7 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf8 = (ctypes.c_ubyte * size)()
buf_p8 = ctypes.cast(buf8, ctypes.c_void_p)
VideoLockCb8 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf9 = (ctypes.c_ubyte * size)()
buf_p9 = ctypes.cast(buf9, ctypes.c_void_p)
VideoLockCb9 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf10 = (ctypes.c_ubyte * size)()
buf_p10 = ctypes.cast(buf10, ctypes.c_void_p)
VideoLockCb10 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf11 = (ctypes.c_ubyte * size)()
buf_p11 = ctypes.cast(buf11, ctypes.c_void_p)
VideoLockCb11 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf12 = (ctypes.c_ubyte * size)()
buf_p12 = ctypes.cast(buf12, ctypes.c_void_p)
VideoLockCb12 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf13 = (ctypes.c_ubyte * size)()
buf_p13 = ctypes.cast(buf13, ctypes.c_void_p)
VideoLockCb13 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf14 = (ctypes.c_ubyte * size)()
buf_p14 = ctypes.cast(buf14, ctypes.c_void_p)
VideoLockCb14 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf15 = (ctypes.c_ubyte * size)()
buf_p15 = ctypes.cast(buf15, ctypes.c_void_p)
VideoLockCb15 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf16 = (ctypes.c_ubyte * size)()
buf_p16 = ctypes.cast(buf16, ctypes.c_void_p)
VideoLockCb16 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf17 = (ctypes.c_ubyte * size)()
buf_p17 = ctypes.cast(buf17, ctypes.c_void_p)
VideoLockCb17 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf18 = (ctypes.c_ubyte * size)()
buf_p18 = ctypes.cast(buf18, ctypes.c_void_p)
VideoLockCb18 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf19 = (ctypes.c_ubyte * size)()
buf_p19 = ctypes.cast(buf19, ctypes.c_void_p)
VideoLockCb19 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))
buf20 = (ctypes.c_ubyte * size)()
buf_p20 = ctypes.cast(buf20, ctypes.c_void_p)
VideoLockCb20 = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_void_p))

global image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,image11,image12,image13,image14,image15,image16,image17,image18,image19,image20
global allow1,allow2,allow3,allow4,allow5,allow6,allow7,allow8,allow9,allow10,allow11,allow12,allow13,allow14,allow15,allow16,allow17,allow18,allow19,allow20
image1 = [1]
image2 = [1]
image3 = [1]
image4 = [1]
image5 = [1]
image6 = [1]
image7 = [1]
image8 = [1]
image9 = [1]
image10 = [1]
image11 = [1]
image12 = [1]
image13 = [1]
image14 = [1]
image15 = [1]
image16 = [1]
image17 = [1]
image18 = [1]
image19 = [1]
image20 = [1]
allow1 = 0
allow2 = 0
allow3 = 0
allow4 = 0
allow5 = 0
allow6 = 0
allow7 = 0
allow8 = 0
allow9 = 0
allow10 = 0
allow11 = 0
allow12 = 0
allow13 = 0
allow14 = 0
allow15 = 0
allow16 = 0
allow17 = 0
allow18 = 0
allow19 = 0
allow20 = 0

@VideoLockCb1
def _lockcb1(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p1

@vlc.CallbackDecorators.VideoDisplayCb
def _display1(opaque, picture):
    global image1
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf1, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image1 = opencvImage
    #cv2.imshow('image1',opencvImage)
    cv2.waitKey(10)

@VideoLockCb2
def _lockcb2(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p2

@vlc.CallbackDecorators.VideoDisplayCb
def _display2(opaque, picture):
    global image2
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf2, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image2 = opencvImage
    #cv2.imshow('image2',opencvImage)
    cv2.waitKey(10)

@VideoLockCb3
def _lockcb3(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p3

@vlc.CallbackDecorators.VideoDisplayCb
def _display3(opaque, picture):
    global image3
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf3, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image3 = opencvImage
    #cv2.imshow('image3',opencvImage)
    cv2.waitKey(10)

@VideoLockCb4
def _lockcb4(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p4

@vlc.CallbackDecorators.VideoDisplayCb
def _display4(opaque, picture):
    global image4
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf4, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image4 = opencvImage
    #cv2.imshow('image4',opencvImage)
    cv2.waitKey(10)

@VideoLockCb5
def _lockcb5(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p5

@vlc.CallbackDecorators.VideoDisplayCb
def _display5(opaque, picture):
    global image5
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf5, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image5 = opencvImage
    #cv2.imshow('image5',opencvImage)
    cv2.waitKey(10)

@VideoLockCb6
def _lockcb6(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p6

@vlc.CallbackDecorators.VideoDisplayCb
def _display6(opaque, picture):
    global image6
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf6, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image6 = opencvImage
    #cv2.imshow('image6',opencvImage)
    cv2.waitKey(10)

@VideoLockCb7
def _lockcb7(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p7

@vlc.CallbackDecorators.VideoDisplayCb
def _display7(opaque, picture):
    global image7
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf7, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image7 = opencvImage
    #cv2.imshow('image7',opencvImage)
    cv2.waitKey(10)

@VideoLockCb8
def _lockcb8(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p8

@vlc.CallbackDecorators.VideoDisplayCb
def _display8(opaque, picture):
    global image8
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf8, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image8 = opencvImage
    #cv2.imshow('image8',opencvImage)
    cv2.waitKey(10)

@VideoLockCb9
def _lockcb9(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p9

@vlc.CallbackDecorators.VideoDisplayCb
def _display9(opaque, picture):
    global image9
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf9, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image9 = opencvImage
    #cv2.imshow('image9',opencvImage)
    cv2.waitKey(10)

@VideoLockCb10
def _lockcb10(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p10

@vlc.CallbackDecorators.VideoDisplayCb
def _display10(opaque, picture):
    global image10
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf10, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image10 = opencvImage
    #cv2.imshow('image10',opencvImage)
    cv2.waitKey(10)

@VideoLockCb11
def _lockcb11(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p11

@vlc.CallbackDecorators.VideoDisplayCb
def _display11(opaque, picture):
    global image11
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf11, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image11 = opencvImage
    #cv2.imshow('image11',opencvImage)
    cv2.waitKey(10)

@VideoLockCb12
def _lockcb12(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p12

@vlc.CallbackDecorators.VideoDisplayCb
def _display12(opaque, picture):
    global image12
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf12, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image12 = opencvImage
    #cv2.imshow('image12',opencvImage)
    cv2.waitKey(10)

@VideoLockCb13
def _lockcb13(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p13

@vlc.CallbackDecorators.VideoDisplayCb
def _display13(opaque, picture):
    global image13
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf13, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image13 = opencvImage
    #cv2.imshow('image13',opencvImage)
    cv2.waitKey(10)

@VideoLockCb14
def _lockcb14(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p14

@vlc.CallbackDecorators.VideoDisplayCb
def _display14(opaque, picture):
    global image14
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf14, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image14 = opencvImage
    #cv2.imshow('image14',opencvImage)
    cv2.waitKey(10)

@VideoLockCb15
def _lockcb15(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p15

@vlc.CallbackDecorators.VideoDisplayCb
def _display15(opaque, picture):
    global image15
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf15, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image15 = opencvImage
    #cv2.imshow('image15',opencvImage)
    cv2.waitKey(10)

@VideoLockCb16
def _lockcb16(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p16

@vlc.CallbackDecorators.VideoDisplayCb
def _display16(opaque, picture):
    global image16
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf16, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image16 = opencvImage
    #cv2.imshow('image16',opencvImage)
    cv2.waitKey(10)

@VideoLockCb17
def _lockcb17(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p17

@vlc.CallbackDecorators.VideoDisplayCb
def _display17(opaque, picture):
    global image17
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf17, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image17 = opencvImage
    #cv2.imshow('image17',opencvImage)
    cv2.waitKey(10)

@VideoLockCb18
def _lockcb18(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p18

@vlc.CallbackDecorators.VideoDisplayCb
def _display18(opaque, picture):
    global image18
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf18, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image18 = opencvImage
    #cv2.imshow('image18',opencvImage)
    cv2.waitKey(10)

@VideoLockCb19
def _lockcb19(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p19

@vlc.CallbackDecorators.VideoDisplayCb
def _display19(opaque, picture):
    global image19
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf19, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image19 = opencvImage
    #cv2.imshow('image19',opencvImage)
    cv2.waitKey(10)

@VideoLockCb20
def _lockcb20(opaque, planes):
    #print("lock", file=sys.stderr)
    planes[0] = buf_p20

@vlc.CallbackDecorators.VideoDisplayCb
def _display20(opaque, picture):
    global image20
    img = Image.frombuffer("RGBA", (VIDEOWIDTH, VIDEOHEIGHT), buf20, "raw", "BGRA", 0, 1)
    opencvImage = cv2.cvtColor(numpy.array(img), cv2.COLOR_RGB2BGR)
    image20 = opencvImage
    #cv2.imshow('image20',opencvImage)
    cv2.waitKey(10)

class Player:
    #播放
    def play(self,url,choose):
        global allow1, allow2, allow3, allow4, allow5, allow6, allow7, allow8, allow9, allow10, allow11, allow12, allow13, allow14, allow15, allow16, allow17, allow18, allow19, allow20
        vlcInstance = vlc.Instance()
        m = vlcInstance.media_new(url)
        self.mp = vlc.libvlc_media_player_new_from_media(m)
        if choose == 1:
            self.mp = vlc.libvlc_media_player_new_from_media(m)
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb1, None, _display1, None)
            allow1 = 1
        if choose == 2:
            self.mp = vlc.libvlc_media_player_new_from_media(m)
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb2, None, _display2, None)
            allow2 = 1
        if choose == 3:
            self.mp = vlc.libvlc_media_player_new_from_media(m)
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb3, None, _display3, None)
            allow3 = 1
        if choose == 4:
            self.mp = vlc.libvlc_media_player_new_from_media(m)
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb4, None, _display4, None)
            allow4 = 1
        if choose == 5:
            self.mp = vlc.libvlc_media_player_new_from_media(m)
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb5, None, _display5, None)
            allow5 = 1
        if choose == 6:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb6, None, _display6, None)
            allow6 = 1
        if choose == 7:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb7, None, _display7, None)
            allow7 = 1
        if choose == 8:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb8, None, _display8, None)
            allow8 = 1
        if choose == 9:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb9, None, _display9, None)
            allow9 = 1
        if choose == 10:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb10, None, _display10, None)
            allow10 = 1
        if choose == 11:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb11, None, _display11, None)
            allow11 = 1
        if choose == 12:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb12, None, _display12, None)
            allow12 = 1
        if choose == 13:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb13, None, _display13, None)
            allow13 = 1
        if choose == 14:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb14, None, _display14, None)
            allow14 = 1
        if choose == 15:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb15, None, _display15, None)
            allow15 = 1
        if choose == 16:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb16, None, _display16, None)
            allow16 = 1
        if choose == 17:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb17, None, _display17, None)
            allow17 = 1
        if choose == 18:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb18, None, _display18, None)
            allow18 = 1
        if choose == 19:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb19, None, _display19, None)
            allow19 = 1
        if choose == 20:
            vlc.libvlc_video_set_callbacks(self.mp, _lockcb20, None, _display20, None)
            allow20 = 1
        self.mp.video_set_format("BGRA", VIDEOWIDTH, VIDEOHEIGHT, VIDEOWIDTH * 4)
        self.mp.play()

    #获取当前帧
    def image_get(self,choose):
        if choose == 1:
            return image1
        if choose == 2:
            return image2
        if choose == 3:
            return image3
        if choose == 4:
            return image4
        if choose == 5:
            return image5
        if choose == 6:
            return image6
        if choose == 7:
            return image7
        if choose == 8:
            return image8
        if choose == 9:
            return image9
        if choose == 10:
            return image10
        if choose == 11:
            return image11
        if choose == 12:
            return image12
        if choose == 13:
            return image13
        if choose == 14:
            return image14
        if choose == 15:
            return image15
        if choose == 16:
            return image16
        if choose == 17:
            return image17
        if choose == 18:
            return image18
        if choose == 19:
            return image19
        if choose == 20:
            return image20

    # 暂停
    def pause(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            self.mp.pause()
    # 恢复
    def resume(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            self.mp.set_pause(0)

    # 停止
    def stop(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            self.mp.stop()

    # 释放资源
    def release(self):
        global allow1, allow2, allow3, allow4, allow5, allow6, allow7, allow8, allow9, allow10, allow11, allow12, allow13, allow14, allow15, allow16, allow17, allow18, allow19, allow20
        if len(image1) != 1 and allow1 == 1:
            allow1 = 0
            return self.mp.release()
        if len(image2) != 1 and allow2 == 1:
            allow2 = 0
            return self.mp.release()
        if len(image3) != 1 and allow3 == 1:
            allow3 = 0
            return self.mp.release()
        if len(image4) != 1 and allow4 == 1:
            allow4 = 0
            return self.mp.release()
        if len(image5) != 1 and allow5 == 1:
            allow5 = 0
            return self.mp.release()
        if len(image6) != 1 and allow6 == 1:
            allow6 = 0
            return self.mp.release()
        if len(image7) != 1 and allow7 == 1:
            allow7 = 0
            return self.mp.release()
        if len(image8) != 1 and allow8 == 1:
            allow8 = 0
            return self.mp.release()
        if len(image9) != 1 and allow9 == 1:
            allow9 = 0
            return self.mp.release()
        if len(image10) != 1 and allow10 == 1:
            allow10 = 0
            return self.mp.release()
        if len(image11) != 1 and allow11 == 1:
            allow11 = 0
            return self.mp.release()
        if len(image12) != 1 and allow12 == 1:
            allow12 = 0
            return self.mp.release()
        if len(image13) != 1 and allow13 == 1:
            allow13 = 0
            return self.mp.release()
        if len(image14) != 1 and allow14 == 1:
            allow14 = 0
            return self.mp.release()
        if len(image15) != 1 and allow15 == 1:
            allow15 = 0
            return self.mp.release()
        if len(image16) != 1 and allow16 == 1:
            allow16 = 0
            return self.mp.release()
        if len(image17) != 1 and allow17 == 1:
            allow17 = 0
            return self.mp.release()
        if len(image18) != 1 and allow18 == 1:
            allow18 = 0
            return self.mp.release()
        if len(image19) != 1 and allow19 == 1:
            allow19 = 0
            return self.mp.release()
        if len(image20) != 1 and allow20 == 1:
            allow20 = 0
            return self.mp.release()

    # 是否正在播放
    def is_playing(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            return self.mp.is_playing()

    # 已播放时间，返回毫秒值
    def get_time(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            return self.mp.get_time()

    # 拖动指定的毫秒值处播放。成功返回0，失败返回-1 (需要注意，只有当前多媒体格式或流媒体协议支持才会生效)
    def set_time(self, ms):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            return self.mp.get_time()

    # 音视频总长度，返回毫秒值
    def get_length(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            return self.mp.get_length()

    # 获取当前音量（0~100）
    def get_volume(self):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            return self.mp.audio_get_volume()

    # 设置音量（0~100）
    def set_volume(self, volume):
        if allow1 == 1 or allow2 == 1 or allow3 == 1 or allow4 == 1 or allow5 == 1 or allow6 == 1 or allow7 == 1 or allow8 == 1 or allow9 == 1 or allow10 == 1 or allow11 == 1 or allow12 == 1 or allow13 == 1 or allow14 == 1 or allow15 == 1 or allow16 == 1 or allow17 == 1 or allow18 == 1 or allow19 == 1 or allow20 == 1:
            return self.mp.audio_set_volume(volume)

if "__main__" == __name__:
    c1 = Player()
    c2 = Player()
    c3 = Player()
    c4 = Player()
    #播放地址选择
    c1.play("C:/Users/zang/Desktop/AI for Video V3.0/video/video_test/test_video1.mp4",1)
    c2.play("C:/Users/zang/Desktop/AI for Video V3.0/video/video_test/test_video1.mp4",2)
    c3.play("C:/Users/zang/Desktop/AI for Video V3.0/video/video_test/test_video1.mp4", 3)
    c4.play("C:/Users/zang/Desktop/AI for Video V3.0/video/video_test/test_video1.mp4",4)
    while True:
        frame = c1.image_get(1)
        if len(frame) != 1:
            cv2.imshow('image1',frame)
            cv2.waitKey(10)

