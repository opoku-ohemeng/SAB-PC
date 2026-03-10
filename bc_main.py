def main():
    pressure = load_pressure_data()

    N_nodes = np.arange(4, 101, 4)
    sec_prob = compute_security_prob(N_nodes)
    latency = compute_latency(N_nodes)

    nominal, attacked, mitigated, velocity = generate_scenarios(pressure)

    
if __name__ == "__main__":
    main()
