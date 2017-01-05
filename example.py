import warnings
import json
warnings.filterwarnings("ignore")
from Tkinter import *

root = Tk()

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)

	# Fingerprint all the mp3's in the directory we give it
	djv.fingerprint_directory("sample1", [".mp3"])

	# Recognize audio from a file
	song = djv.recognize(FileRecognizer, "sample1/egg_dropping.mp3")
	print "Artificial Delay"
	print "From file we recognized: %s\n" % song
	
	
	w= Label(root, text="From file we recognized: %s\n" % song)
	w.pack()
	root.mainloop()
	# Or recognize audio from your microphone for `secs` seconds
	secs = 5
	song = djv.recognize(MicrophoneRecognizer, seconds=secs)
	
	# Or use a recognizer without the shortcut, in anyway you would like
	recognizer = FileRecognizer(djv)
	song = recognizer.recognize_file("sample1/egg_dropping.mp3")
	print "No shortcut, we recognized: %s\n" % song
