#!/usr/bin/python
import sys
import Leap
from Tone import Tone

class ThereminListener(Leap.Listener):
	def __init__(self, tone = None):
		Leap.Listener.__init__(self)
		self.tone = tone
		
	def on_frame(self, controller):
		# Get the most recent frame and report some basic information
		frame = controller.frame()

		if frame.hands.empty:
			self.tone.setAmplitude(0)
		else:
			# Get the first hand
			hand = frame.hands[0]

			#amp = hand.sphere_radius / 100 + 0.5
			amp = 1.5 - abs(hand.palm_position[1]) / 200
			if amp > 1.0:
				amp = 1.0
			if amp < 0:
				amp = 0
			freq = 220 * (2 ** (abs(hand.palm_position[0] + 200) / 200)) 
			self.tone.setAmplitude(amp)
			self.tone.setFrequency(freq)

def main():
	t = Tone()
	t.open()
	t.setAmplitude(0)
	t.start()

	# Create a sample listener and controller
	listener = ThereminListener(t)
	controller = Leap.Controller()

	# Have the sample listener receive events from the controller
	controller.add_listener(listener)

	# Keep this process running until Enter is pressed
	print "Press Enter to quit..."
	sys.stdin.readline()

	# Remove the sample listener when done
	controller.remove_listener(listener)

	t.stop()
	t.close()

if __name__ == "__main__":
    main()
