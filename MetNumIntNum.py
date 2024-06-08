import numpy as np
import time
import matplotlib.pyplot as plt

def simpson_13(a, b, N):
    h = (b - a) / N
    x = np.linspace(a, b, N + 1)
    y = 4 / (1 + x**2)
    S = y[0] + y[-1]

    for i in range(1, N, 2):
        S += 4 * y[i]
    for i in range(2, N, 2):
        S += 2 * y[i]

    return (h / 3) * S

def rmsError(estimated, reference):
    return np.sqrt(np.mean((estimated - reference)**2))

def kalkulasi():
    reference_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]
    results = []

    for N in N_values:
        start_time = time.time()
        estimated_pi = simpson_13(0, 1, N)
        end_time = time.time()
        
        error = rmsError(estimated_pi, reference_pi)
        exec_time = end_time - start_time
        
        results.append((N, estimated_pi, error, exec_time))
        print(f"N = {N}: Estimated π = {estimated_pi}, RMS Error = {error}, Execution Time = {exec_time:.10f} seconds")

    return results

def plot_results(results):
    N_values = [result[0] for result in results]
    estimated_pis = [result[1] for result in results]
    errors = [result[2] for result in results]
    exec_times = [result[3] for result in results]

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.plot(N_values, estimated_pis, 'o-', label='Estimated π')
    plt.axhline(y=3.14159265358979323846, color='r', linestyle='--', label='Reference π')
    plt.xscale('log')
    plt.xlabel('N')
    plt.ylabel('Estimated π')
    plt.legend()
    plt.title('Estimated π vs N')
    plt.subplot(1, 3, 2)
    plt.plot(N_values, errors, 'o-', label='RMS Error')
    plt.xscale('log')
    plt.xlabel('N')
    plt.ylabel('RMS Error')
    plt.legend()
    plt.title('RMS Error vs N')
    plt.subplot(1, 3, 3)
    plt.plot(N_values, exec_times, 'o-', label='Execution Time (s)')
    plt.xscale('log')
    plt.xlabel('N')
    plt.ylabel('Execution Time (s)')
    plt.legend()
    plt.title('Execution Time vs N')
    plt.tight_layout()
    plt.show()


hasil_kalkulasi = kalkulasi()
plot_results(hasil_kalkulasi)