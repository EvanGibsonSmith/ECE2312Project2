import librosa
import matplotlib.pyplot as plt
import numpy as np

pathname = "EncountersOfTheThirdKind.wav"
data, sampling_rate = librosa.load("Sound Recordings/" + pathname, sr = 44100)

freq = librosa.amplitude_to_db(np.abs(librosa.stft(data)), ref=np.max)
print(freq.shape)

# not sure of exact c map from the lecture
# below modified from librosa documentation https://librosa.org/doc/main/auto_examples/plot_display.html
fig, ax = plt.subplots()
img = librosa.display.specshow(freq, x_axis='time', y_axis='linear', cmap='nipy_spectral', ax=ax)
ax.set(title='Spectogram of ' + pathname, ylim=[0, 8000]) # TODO fix naming
fig.colorbar(img, ax=ax, format="%+2.f dB")

plt.show()
 