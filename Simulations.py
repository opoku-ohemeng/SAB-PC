import numpy as np
from .model import A, B
from .controllers import Acl_baseline, Acl_sab
from .metrics import spectral_radius

def compute_rho_samples(K_base_modes, K_sab_modes, Pi_n, delay_samples):
    num_samples = len(delay_samples)
    baseline_rhos = np.zeros(num_samples)
    sabpc_rhos    = np.zeros(num_samples)

    modes = np.arange(3)

    for i in range(num_samples):
        m = np.random.choice(modes, p=Pi_n)
        d = delay_samples[i]

        A_eff_base = Acl_baseline(A, B, K_base_modes[m])
        A_eff_sab  = Acl_sab(A, B, K_sab_modes[m], d)

        baseline_rhos[i] = spectral_radius(A_eff_base)
        sabpc_rhos[i]    = spectral_radius(A_eff_sab)

    return baseline_rhos, sabpc_rhos
