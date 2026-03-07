import numpy as np

def get_delay_samples(n, num_samples):
    mean_ms = 40 + 3.0 * np.log1p(n)
    std_ms  = 5 + 0.5 * np.log1p(n)

    delays_ms = np.random.normal(mean_ms, std_ms, size=num_samples)
    delays_ms = np.clip(delays_ms, 0, None)

    return np.round(delays_ms / 100.0).astype(int)
