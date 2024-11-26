import numpy as np
from queueing_tool.markov import dtmc_steady_state, dtmcfpt

# Matriz de transição
A = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [0.2, 0.3, 0.4, 0.1],
    [0.3, 0.4, 0.2, 0.1],
    [0.25, 0.25, 0.25, 0.25]
])

# Distribuição estacionária teórica usando queueing-tool
stationary_distribution_theoretical = dtmc_steady_state(A)
print("Distribuição estacionária teórica:", stationary_distribution_theoretical)

# Calcule a distribuição estacionária pela simulação
def simulate_stationary_distribution(A, steps=100000):
    n_states = A.shape[0]
    state_counts = np.zeros(n_states)
    state = 0  # Estado inicial
    for _ in range(steps):
        state = np.random.choice(len(A), p=A[state])
        state_counts[state] += 1
    stationary_distribution_simulated = state_counts / steps
    return stationary_distribution_simulated

stationary_distribution_simulated = simulate_stationary_distribution(A, steps=100000)
print("Distribuição estacionária simulada:", stationary_distribution_simulated)

# Comparação entre a distribuição estacionária teórica e simulada
print("Diferença entre teórica e simulada:", stationary_distribution_theoretical - stationary_distribution_simulated)

# Cálculo teórico do tempo médio de recorrência do estado 0 para o estado 3 usando dtmcfpt
mean_recurrence_time_theoretical = dtmcfpt(A, 0, 3)
print("Tempo médio de recorrência teórico (estado 0 para estado 3):", mean_recurrence_time_theoretical)

# Cálculo do tempo médio de recorrência pela simulação
def calculate_mean_recurrence_time(A, start_state, target_state, max_steps=100000):
    total_recurrence_time = 0
    recurrence_count = 0
    state = start_state
    steps = 0

    while recurrence_count < max_steps:
        state = np.random.choice(len(A), p=A[state])
        steps += 1
        if state == target_state:
            total_recurrence_time += steps
            recurrence_count += 1
            steps = 0  # Reinicie o contador para a próxima recorrência

    mean_recurrence_time_simulated = total_recurrence_time / recurrence_count
    return mean_recurrence_time_simulated

mean_recurrence_time_simulated = calculate_mean_recurrence_time(A, start_state=0, target_state=3)
print("Tempo médio de recorrência simulado (estado 0 para estado 3):", mean_recurrence_time_simulated)

# Comparação entre o tempo médio de recorrência teórico e simulado
print("Diferença entre tempo médio teórico e simulado:", mean_recurrence_time_theoretical - mean_recurrence_time_simulated)
