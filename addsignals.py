import librosa
from scipy.io.wavfile import write

rootFolder = "Sound Recordings/"
pathname1 = "SmithBechwati-quick_brown_fox.wav"
data1, sampling_rate1 = librosa.load(rootFolder + pathname1, sr = 44100)

pathname2 = "SmithBechwati-chirp.wav"
data2, sampling_rate2 = librosa.load(rootFolder + pathname2, sr = 44100)

outPathname = "SmithBechwait-quick_brown_fox_chirp.wav"
if (sampling_rate1!=sampling_rate2):
    print("Sampling Rates are not equal!")

else:
    write(rootFolder + outPathname, sampling_rate1, data1+data2) # sampling rates are same so selecting either is fine