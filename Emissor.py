from signalTeste import *
from apoioemissor import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
#import wave
import time
import pickle
import peakutils

com = comunicador()

tempo, onda = com.comunica(1)

plotaonda(tempo, onda)
