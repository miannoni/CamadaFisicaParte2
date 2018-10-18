from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
import pickle
import peakutils
from apoioemissor import *

dicionario_digitos = {
			1 : [697, 1209],
			2 : [697, 1366],
			3 : [697, 1477],
			4 : [770, 1209],
			5 : [770, 1366],
			6 : [770, 1477],
			7 : [852, 1209],
			8 : [852, 1366],
			9 : [852, 1477],
			0 : [941, 1366]}

fs = 44100
duration = 1 #segundos

time = duration

n = time*fs
x = np.linspace(0.0, time, n)

while True:

	myrecording = sd.rec(int(n), samplerate=fs, channels=1)[:,0]
	x = np.linspace(0.0, time, n)

	sd.wait()

	plt.plot(x, myrecording)
	plt.title('Onda de chegada')
	plt.show()

	sinal = signalMeu()
	x, y = sinal.calcFFT(myrecording, fs)
	# sinal.plotFFT(myrecording,fs)

	picos = peakutils.indexes(y, thres=0.6, min_dist=30, thres_abs=False)

	z = x

	val1 = 0
	idx1 = 0
	val2 = 0
	idx2 = 0

	for x in range(len(picos)):

		if z[picos[x]] >= val1:
			val1 = z[picos[x]]
			idx1 = x
	
	plt.plot(z[picos[idx1]], y[picos[idx1]], 'ro')

	for x in range(len(picos)):

		if z[picos[x]] >= val2:
			if x != idx1:
				val2 = z[picos[x]]
				idx2 = x

	plt.plot(z[picos[idx2]], y[picos[idx2]], 'ro')

	flag = False

	for x in range(10):

		delta1 = (val1 - dicionario_digitos[x][1])#**2)**0.5
		delta2 = (val2 - dicionario_digitos[x][0])#**2)**0.5

		if delta1 < 0:
			delta1 *= -1
		if delta2 < 0:
			delta2 *= -1

		# print("character, delta 1: {}, {}".format(x, delta1))
		# print("character, delta 2: {}, {}".format(x, delta2))

		if ((delta1 < dicionario_digitos[x][1]*0.05) and (delta2 < dicionario_digitos[x][0]*0.05) and (flag == False)):
			print("Frequencias de pico encontradas: {}Hz, {}Hz".format(val1, val2))
			print("É o numero {}".format(x))
			flag = True

	plt.plot(z, y)
	plt.title('Fourier')
	plt.show()

	if flag == False:
		print("Frequencias de pico encontradas: {}Hz, {}Hz".format(val1, val2, 2))
		print("Não encontrei um numero!")