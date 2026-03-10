def load_pressure_data(n_samples=1000):
    path = kagglehub.dataset_download("averkij/tennessee-eastman-process-simulation-dataset")
    file_path = os.path.join(path, "TEP_FaultFree_Training.RData")

    result = pyreadr.read_r(file_path)
    tep_df = result['fault_free_training']

    pressure_raw = tep_df['xmeas_7'].values[:n_samples]
    pressure_baseline = (pressure_raw - np.mean(pressure_raw)) * 5

    return pressure_baseline
