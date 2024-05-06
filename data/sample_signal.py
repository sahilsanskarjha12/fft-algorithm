import numpy as np

# Sample signal generation parameters
fs = 1000  # Sampling frequency (Hz)
duration = 1  # Duration of the signal (seconds)
t = np.linspace(0, duration, int(fs * duration), endpoint=False)  # Time array

# Define frequencies of sinusoidal components
frequencies = [50, 120]

# Generate the composite signal
composite_signal = np.sum([np.sin(2 * np.pi * f * t) for f in frequencies], axis=0)

# Save the composite signal as a NumPy array in a file
np.save('data/sample_signal.npy', composite_signal)
