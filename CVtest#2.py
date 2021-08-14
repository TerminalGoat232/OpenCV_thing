import pyautogui as pag
from FLIB import *
import cv2
import numpy as np
import serial as sr
# setup
for x in range(0,10):
	try:
		ADS = sr.Serial('COM{x}', 9600)
		tmdprint("your serial port is COM{x}")
	except: pass
def shit():
	img = pag.screenshot('shitIMG.png', region=(500,400, 800, 500))
	HSVCOLOR = cv2.cvtColor(np.float32(img), cv2.COLOR_BGR2HSV)
	lwr1 = np.array([49,0,97], np.uint8)
	upr1 = np.array([84,105,255], np.uint8)
	lwr2 = np.array([89, 0, 97], np.uint8)
	upr2 = np.array([84,195,194], np.uint8)

	msk = cv2.inRange(HSVCOLOR, lwr1, upr1)
	msk2 = cv2.inRange(HSVCOLOR, lwr2,  upr2)
	cv2.imwrite('shitIMG.png', msk)
	#cv2.imwrite('shitIMG.png', msk2)
	#cv2.imshow('shit2', msk2)
	cv2.imshow('shit', msk)
	cv2.imshow('shit2', np.uint8(img))
	k = cv2.countNonZero(msk)
	#kk = cv2.countNonZero(msk2)

	print('bit needed[cyan]:', k)
	#print('bit needed[brown]:', kk)
	if k >= 5002:
		print('found some thing CYAN')
		ADS.write(str.encode('1')) 
	else : ADS.write(str.encode('0'))

	#if kk >= 7042:
		#print('found some thing brown')

while(1):
	shit()
	if cv2.waitKey(1) & 0xFF == ord('e'):
		cv2.destroyAllWindows()
		break
