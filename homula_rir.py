# HOMULA-RIR sample code
# Author: Federico Miotello (federico.miotello@polimi.it)
# Date: April 9th, 2024


import os
import csv
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

BASE_DIR = 'HOMULA-RIR'  # Path to dataset folder


# Read a RIR

wav_file = 'hom/row3/rir-S1-R3-HOM2.wav'
fs, rir = wavfile.read(os.path.join(BASE_DIR, wav_file))  # Reading RIR between source S1 and HOM 2 in 3rd row


# Plot a RIR

ch = 1  # Channel within the microphone array
samples_to_plot = int(0.1*fs)  # Plotting the first 0.1 secs

length = rir.shape[0]/fs
time_ax = np.linspace(0., length, rir.shape[0])
plt.plot(time_ax[0:samples_to_plot], rir[0:samples_to_plot,ch])
plt.show()


# Plot source and mic positions in 3D

# Room dimensions
x_dim = [0, 5.46]
y_dim = [0, 14.52]
z_dim = [0, 3.38]

sources_pos = np.genfromtxt(os.path.join(BASE_DIR, 'pos-sources.csv'), delimiter=",")[1:]
mic_pos = np.genfromtxt(os.path.join(BASE_DIR, 'hom/row3/pos-R3-HOM2.csv'), delimiter=",")[1:]

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(mic_pos[:, 0], mic_pos[:, 1], mic_pos[:, 2])
ax.scatter(sources_pos[1, 0], sources_pos[1, 1], sources_pos[1, 2])

ax.set_xlim(x_dim[1], x_dim[0])  # Inverted axis to reproduce real room setup
ax.set_ylim(y_dim)
ax.set_zlim(z_dim)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()



