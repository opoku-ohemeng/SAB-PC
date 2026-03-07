import numpy as np

def Pi(n):
    p1 = max(0.85 - 0.02*n, 0.05)
    p2 = min(0.10 + 0.015*n, 0.60)
    p3 = 1 - p1 - p2
    return np.array([p1, p2, p3])
