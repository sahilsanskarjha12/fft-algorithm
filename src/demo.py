import matplotlib.pyplot as plt

# Generate a sample signal
N = 1000
t = np.linspace(0, 1, N, endpoint=False)
x = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Compute FFT of the signal
X = fft(x)

# Plot the signal and its FFT
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.subplot(2, 1, 2)
frequencies = np.fft.fftfreq(N, 1/N)
plt.plot(frequencies[:N//2], np.abs(X[:N//2]))
plt.title('FFT of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()
