from .metrics import compute_security_prob, compute_latency, compute_velocity

def generate_scenarios(pressure):
    nominal = pressure[:500]
    attacked = nominal.copy()
    attacked[200:400] += 8.0

    mitigated = nominal.copy()
    mitigated[200:400] += 1.2

    velocity = compute_velocity(nominal)
    return nominal, attacked, mitigated, velocity
