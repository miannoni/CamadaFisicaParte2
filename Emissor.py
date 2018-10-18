from signalTeste import *
from apoioemissor import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
from msvcrt import getch
import time
import pickle
import keyboard
import peakutils

com = comunicador()

while True:

	if keyboard.is_pressed('0'):
		com.comunica(0)

	if keyboard.is_pressed('1'):
		com.comunica(1)

	if keyboard.is_pressed('2'):
		com.comunica(2)

	if keyboard.is_pressed('3'):
		com.comunica(3)

	if keyboard.is_pressed('4'):
		com.comunica(4)

	if keyboard.is_pressed('5'):
		com.comunica(5)

	if keyboard.is_pressed('6'):
		com.comunica(6)

	if keyboard.is_pressed('7'):
		com.comunica(7)

	if keyboard.is_pressed('8'):
		com.comunica(8)

	if keyboard.is_pressed('9'):
		com.comunica(9)

	if keyboard.is_pressed('q'):
		break