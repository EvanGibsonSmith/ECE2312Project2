import librosa
import numpy as np
from scipy.io.wavfile import write
from scipy import signal

order = 20 # make the order extemely high because we have no constraints
fc = 4000

rootFolder = "Sound Recordings/"

#Filtering Chirp Sound
pathname1 = "SmithBechwati-quick_brown_fox_chirp.wav"
data1, sampling_rate1 = librosa.load(rootFolder + pathname1, sr = 44100)

sos1 = signal.butter(order, 2000, btype='low', analog=False, output='sos', fs=sampling_rate1)
filtered1 = signal.sosfiltfilt(sos1, data1)

outPathname1 = "SmithBechwati-filteredspeechchirp-2000HzLowcutoff.wav"
write(rootFolder + outPathname1, sampling_rate1, filtered1.astype(np.float32))

# Filtering Chirp Sound, attempting band pass (doesn't work very well)
pathname2 = "SmithBechwati-quick_brown_fox_chirp.wav"
data2, sampling_rate2 = librosa.load(rootFolder + pathname2, sr = 44100)

fcHigh = 500
sosLow2 = signal.butter(order, fc, btype='low', analog=False, output='sos', fs=sampling_rate2)  
sosHigh2 = signal.butter(order, fcHigh, btype='high', analog=False, output='sos', fs=sampling_rate2)  
filtered2 = signal.sosfiltfilt(sosHigh2, signal.sosfiltfilt(sosLow2, data2))

outPathname2 = "SmithBechwati-filteredspeechchirp-bandpass.wav"
write(rootFolder + outPathname2, sampling_rate2, filtered2.astype(np.float32))

#Filtering Sine Tone Sound
pathname3 = "SmithBechwati-quick_brown_fox_sinetone.wav"
data3, sampling_rate3 = librosa.load(rootFolder + pathname3, sr = 44100)

sos3 = signal.butter(order, fc, btype='low', analog=False, output='sos', fs=sampling_rate3)
filtered3 = signal.sosfiltfilt(sos3, data3)

outPathname3 = "SmithBechwati-filteredspeechsinetone.wav"
write(rootFolder + outPathname3, sampling_rate3, filtered3.astype(np.float32))
