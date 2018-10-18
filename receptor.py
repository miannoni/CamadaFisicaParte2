from signalTeste import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
import pickle
import peakutils
from apoioemissor import *

fs = 44100
duration = 0.1 #segundos

time = duration

n = time*fs
x = np.linspace(0.0, time, n)

myrecording = sd.rec(int(n), samplerate=fs, channels=1)[:,0]
print(myrecording)
sd.wait()

sinal = signalMeu()
x,y  = sinal.calcFFT(myrecording, fs)
# plotaonda(x,y[:,0])
sinal.plotFFT(myrecording,fs)
# plotaonda(x,myrecording)
