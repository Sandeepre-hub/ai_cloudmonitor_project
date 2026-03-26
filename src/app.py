import numpy as np
import os

def detect_anomaly(data):
    mean = np.mean(data)
    std = np.std(data)
    latest = data[-1]

    if latest > mean + 2 * std:
        return True
    return False

def remediate():
    print("⚠️ Anomaly detected! Restarting pod...")
    os.system("echo 'Simulating pod restart...'")

if __name__ == "__main__":
    sample_data = [10, 12, 11, 13, 50]

    if detect_anomaly(sample_data):
        remediate()
    else:
        print("System normal")