import librosa
from scipy.io.wavfile import write

rootFolder = "Sound Recordings/"
pathname1 = "SmithBechwati-quick_brown_fox.wav"
data1, sampling_rate1 = librosa.load(rootFolder + pathname1, sr = 44100)

#Adding Chirp
pathname2 = "SmithBechwati-chirp.wav"
data2, sampling_rate2 = librosa.load(rootFolder + pathname2, sr = 44100)

outPathname1 = "SmithBechwati-quick_brown_fox_chirp.wav"
if (sampling_rate1!=sampling_rate2):
    print("Sampling Rates are not equal!")

else:
    write(rootFolder + outPathname1, sampling_rate1, data1+data2) # sampling rates are same so selecting either is fine

#Adding Sine Tone
pathname3 = "SmithBechwati-sinetone.wav"
data3, sampling_rate3 = librosa.load(rootFolder + pathname3, sr = 44100)
outPathname3 = "SmithBechwati-quick_brown_fox_sinetone.wav"
if (sampling_rate1!=sampling_rate2):
    print("Sampling Rates are not equal!")

else:
    write(rootFolder + outPathname3, sampling_rate1, data1+data3)
