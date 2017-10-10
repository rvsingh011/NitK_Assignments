import numpy as np


def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)      #convert into array
    N = x.shape[0]                      #find dimension of array
    n = np.arange(N)                    #create a array in range(N)
    k = n.reshape((N, 1))               #Create a list of list for this [[0][1]..
    M = np.exp(-2j * np.pi * k * n / N) #generate expontial
    return np.dot(M, x)


def FFT(x):
    """A recursive implementation of the 1D Cooley-Tukey FFT"""
    x = np.asarray(x, dtype=float)
    N = x.shape[0]

    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N) / N)
        return np.concatenate([X_even + factor[:int(N/2)] * X_odd,
                               X_even + factor[int(N/2):] * X_odd])
x = np.random.random(1024)

print(np.allclose(FFT(x), np.fft.fft(x)))
print(FFT(x))