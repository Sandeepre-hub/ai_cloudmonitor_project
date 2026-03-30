import numpy as np
import os

def detect_anomaly(data):
    mean = np.mean(data)
    std = np.std(data)
    latest = data[-1]

    if latest > 50:
        return True
    return False

def remediate():
    print("Anomaly detected! Restarting pod...")
    os.system("kubectl delete pod -l app=demo")

if __name__ == "__main__":
    sample_data = [10, 12, 11, 13, 200]

    if detect_anomaly(sample_data):
        remediate()
    else:
        print("System normal")