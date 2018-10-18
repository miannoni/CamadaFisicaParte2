from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
import pickle
import peakutils

sinal = signalMeu()

freq = 1209
amplitude = 1
fs = 44100
time = 
tempo, onda = sinal.generateSin(freq, amplitude, time, fs)

x,y = [tempo,onda]

plt.figure()
plt.plot(x, np.abs(y))
# plt.axis([min(x),max(x), min(np.abs(y)), max(np.abs(y))])
plt.xlim([min(x),max(x)])
plt.ylim([min(np.abs(y)),max(np.abs(y))])
plt.title('Fourier')
plt.show()
