from signalTeste import *

def plotaonda(tempo, onda):
	x,y = [tempo,onda]
	plt.figure()
	plt.plot(x, np.abs(y))
	plt.xlim([min(x),max(x)])
	plt.ylim([min(np.abs(y)),max(np.abs(y))])
	plt.title('Fourier')
	plt.show()

class comunicador():

	def __init__(self):
		self.dicionario_digitos = {
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
		self.sinal = signalMeu()
		self.amplitude = 1
		self.fs = 44100
		self.time = 1

	def sinalDigito(self, digito):

		freq1, freq2 = self.dicionario_digitos[digito]

		tempo, onda = self.sinal.generateSin(freq1, self.amplitude, self.time, self.fs)

		tempo, onda2 = self.sinal.generateSin(freq2, self.amplitude, self.time, self.fs)

		onda = np.add(np.array(onda), np.array(onda2))

		return (tempo, onda)

	def comunica(self, digito):
		tempo, onda = self.sinalDigito(digito)

		plotaonda(tempo, onda)

		sd.play(onda, self.fs)

		sd.wait()

		return (tempo, onda)