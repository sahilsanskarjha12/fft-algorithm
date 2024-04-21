import numpy as np

def fft(x):
    """Compute the 1D Fast Fourier Transform of input signal x."""
    N = len(x)
    if N <= 1:
        return x
    even_fft = fft(x[::2])
    odd_fft = fft(x[1::2])
    factor = np.exp(-2j * np.pi * np.arange(N) / N)
    return np.concatenate([even_fft + factor[:N//2] * odd_fft,
                           even_fft + factor[N//2:] * odd_fft])

def ifft(X):
    """Compute the 1D Inverse Fast Fourier Transform of frequency-domain signal X."""
    N = len(X)
    if N <= 1:
        return X
    even_ifft = ifft(X[::2])
    odd_ifft = ifft(X[1::2])
    factor = np.exp(2j * np.pi * np.arange(N) / N)
    return np.concatenate([even_ifft + factor[:N//2] * odd_ifft,
                           even_ifft + factor[N//2:] * odd_ifft]) / 2

