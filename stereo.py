import librosa
import numpy as np
from scipy.io.wavfile import write

rootFolder = "Sound Recordings/"
pathname1 = "SmithBechwati-quick_brown_fox.wav"
left, sampling_rate1 = librosa.load(rootFolder + pathname1, sr = 44100)

pathname2 = "SmithBechwati-quick_brown_fox_sinetone.wav"
right, sampling_rate2 = librosa.load(rootFolder + pathname2, sr = 44100)

stereo_data = np.array([np.asarray(left), np.asarray(right)])
out_pathname = "SmithBechwati-stereospeechsine.wav"
write(rootFolder + out_pathname, sampling_rate1, stereo_data.T.astype(np.float32))