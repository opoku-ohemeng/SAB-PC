import numpy as np
from numpy.linalg import eigvals

def spectral_radius(M):
    return max(abs(eigvals(M)))
