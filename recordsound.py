import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import matplotlib.pyplot as plt

def sinSignal(x):
    return np.sin(5000*2*np.pi*x)

def chirpSignal(x):
    freq = (8000/5)*x # line equation corresponding to a line between 0 hz and 8000 hz from time 0 to 5
    return np.sin(freq*2*np.pi*x)

pathname = "SmithBechwati-sinetone.wav"
# Define Sampling Rate or Frequency in HzW
sr = 44100

# Record duration in seconds
duration = 5

# Start audio recording
timesteps = np.linspace(0, 5, num=5*sr)
print(timesteps)
recording = np.array([sinSignal(x) for x in timesteps]).astype(np.float32)

plt.plot(recording)
plt.show()

# Write it to a file
path = "Sound Recordings/" + pathname
write(path, sr, recording)