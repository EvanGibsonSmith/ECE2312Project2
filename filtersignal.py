import librosa
import numpy as np
from scipy.io.wavfile import write
from scipy import signal

order = 3
fc = 4000

rootFolder = "Sound Recordings/"

#Filtering Chirp Sound
pathname1 = "SmithBechwati-quick_brown_fox_chirp.wav"
data1, sampling_rate1 = librosa.load(rootFolder + pathname1, sr = 44100)

sos1 = signal.butter(order, fc, btype='low', analog=False, output='sos', fs=sampling_rate1)
filtered1 = signal.sosfiltfilt(sos1, data1)

outPathname1 = "SmithBechwati-filteredspeechchirp.wav"
write(rootFolder + outPathname1, sampling_rate1, filtered1)

#Filtering Sine Tone Sound
pathname2 = "SmithBechwati-quick_brown_fox_sinetone.wav"
data2, sampling_rate2 = librosa.load(rootFolder + pathname2, sr = 44100)

sos2 = signal.butter(order, fc, btype='low', analog=False, output='sos', fs=sampling_rate2)
filtered2 = signal.sosfiltfilt(sos2, data2)

outPathname2 = "SmithBechwati-filteredspeechsinetone.wav"
write(rootFolder + outPathname2, sampling_rate2, filtered2)
