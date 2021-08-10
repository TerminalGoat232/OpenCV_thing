from cv2 import *
from numpy import *
from pyautogui import *
from tkinter import *
from time import *
scr_size=(1920, 1080)
FPS = 15
C = VideoWriter_fourcc(*"XVID")
output = VideoWriter("o.avi", C, FPS ,(scr_size))
namedWindow("RECORDING", WINDOW_NORMAL)
resizeWindow("RECORDING", 800, 700 )
while True:
	i =  screenshot()
	fm = array(i)
	fme = cvtColor(fm, COLOR_BGR2RGB)
	imshow('RECORDING', fme)
	output.write(fme)
	sleep(0.00000000000000000000001)
	if waitKey(1) & 0xFF == ord('e'):
		break

#output.release()
destroyAllWindows()