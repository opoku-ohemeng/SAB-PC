import numpy as np

from sabpc_sim.controllers import K_base_modes, K_sab_modes
from sabpc_sim.delays import get_delay_samples
from sabpc_sim.mjls import Pi
from sabpc_sim.simulation import compute_rho_samples
from sabpc_sim.plotting import plot_results

n_vals = np.arange(4, 21, 2)
samples = 400

baseline_rhos_samples = []
sabpc_rhos_samples    = []
delay_mean = []
delay_std  = []

for n in n_vals:
    Pi_n = Pi(n)
    delays = get_delay_samples(n, samples)

    base_rho, sab_rho = compute_rho_samples(
        K_base_modes, K_sab_modes, Pi_n, delays
    )

    baseline_rhos_samples.append(base_rho)
    sabpc_rhos_samples.append(sab_rho)

    delay_mean.append(np.mean(delays))
    delay_std.append(np.std(delays))

baseline_rhos_samples = np.array(baseline_rhos_samples)
sabpc_rhos_samples    = np.array(sabpc_rhos_samples)
delay_mean = np.array(delay_mean)
delay_std  = np.array(delay_std)

baseline_mean = baseline_rhos_samples.mean(axis=1)
baseline_std  = baseline_rhos_samples.std(axis=1)
sabpc_mean    = sabpc_rhos_samples.mean(axis=1)
sabpc_std     = sabpc_rhos_samples.std(axis=1)

plot_results(n_vals, baseline_mean, baseline_std,
             sabpc_mean, sabpc_std, delay_mean, delay_std)
