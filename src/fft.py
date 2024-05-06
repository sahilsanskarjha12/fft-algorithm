import numpy as np
import matplotlib.pyplot as plt

# Sample signal generation
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1/fs)  # Time array (1 second duration)
f1 = 50  # Frequency of the first sinusoidal component (Hz)
f2 = 120  # Frequency of the second sinusoidal component (Hz)
x = np.sin(2 * np.pi * f1 * t) + 0.5 * np.sin(2 * np.pi * f2 * t)  # Composite signal

# Compute FFT
X = np.fft.fft(x)
freqs = np.fft.fftfreq(len(x), 1/fs)  # Frequency axis

# Plot the original signal and its FFT
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freqs[:len(x)//2], np.abs(X[:len(x)//2]))
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()
