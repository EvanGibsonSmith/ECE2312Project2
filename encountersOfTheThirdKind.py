import numpy as np
from math import floor
from scipy.io.wavfile import write

# create signal based on pure sin waves
sinHz = [470, 525, 415, 205, 310] # initially an octave too low
sinHz = [elem*2 for elem in sinHz]
durations = [0.8, 1, 1.5, 1, 2.5] # intiially too slow
durations = [elem*0.75 for elem in durations] # make a little faster

sr = 44000

output = []
for noteIndex in range(len(sinHz)):
    noteSinHz = sinHz[noteIndex]
    noteDuration = durations[noteIndex]
    output += [np.sin(2*np.pi*noteSinHz*t) for t in np.linspace(0, noteDuration, num=floor(noteDuration*sr))]

output = np.array(output).astype(np.float32)

# save signal in recording
# Write it to a file
pathname = "SmithBechwati-cetk.wav"
path = "Sound Recordings/" + pathname
write(path, sr, output)
