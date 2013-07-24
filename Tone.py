#!/usr/bin/env python
import math
import array
import pyaudio
import threading

class Tone:
	def __init__(self, rate = 44100, frequency = 440.0, amplitude = 1.0):
		self.rate = rate
		self.freq = frequency
		self.amp = amplitude
		self.phase = 0.0
		
	def open(self):
		self.p = pyaudio.PyAudio()
		self.stream = self.p.open(rate=int(self.rate), channels=1, format=pyaudio.paFloat32, output=True)

	def close(self):
		self.stream.close()
		self.p.terminate()
		
	def setAmplitude(self, amp):
		self.amp = amp

	def setFrequency(self, freq):
		self.freq = freq
	
	def start(self):
		self.t = threading.Thread(target=self.run)
		self.t.daemon = True
		self.running = True
		self.t.start()
		
	def stop(self):
		self.running = False
		self.t.join()
		
	def run(self):
		def gen():
			for i in xrange(int(self.rate * 0.05)):
				yield math.sin(self.phase) * self.amp
				self.phase += 2. * math.pi * self.freq / self.rate
				if self.phase > math.pi:
					self.phase -= 2. * math.pi

		while self.running:
			buf = array.array('f', gen()).tostring()
			self.stream.write(buf)

if __name__ == '__main__':
	import time
	t = Tone(frequency = 462)
	t.open()
	t.start()
	time.sleep(2)
	t.stop()
	t.close()
