import numpy as np

# Defina a matriz de transição
A = np.array([
    [0.1, 0.2, 0.3, 0.4],
    [0.2, 0.3, 0.4, 0.1],
    [0.3, 0.4, 0.2, 0.1],
    [0.25, 0.25, 0.25, 0.25]
])

# Função para movimentar entre estados com base nas probabilidades de transição
def markov_move(A, s):
    probs = A[s]
    return np.random.choice(len(probs), p=probs)

# Simulação para encontrar o regime estacionário
def simulate_stationary_distribution(A, steps=100000):
    n_states = A.shape[0]
    state_counts = np.zeros(n_states)
    state = 0  # Estado inicial
    for _ in range(steps):
        state = markov_move(A, state)
        state_counts[state] += 1
    stationary_distribution = state_counts / steps
    return stationary_distribution

# Cálculo do tempo médio de recorrência
def calculate_mean_recurrence_time(A, start_state, target_state, max_steps=100000):
    total_recurrence_time = 0
    recurrence_count = 0
    state = start_state
    steps = 0

    while recurrence_count < max_steps:
        state = markov_move(A, state)
        steps += 1
        if state == target_state:
            total_recurrence_time += steps
            recurrence_count += 1
            steps = 0  # Reinicie o contador para a próxima recorrência

    mean_recurrence_time = total_recurrence_time / recurrence_count
    return mean_recurrence_time

# Simulação de 100000 passos para regime estacionário
stationary_distribution = simulate_stationary_distribution(A, steps=100000)
print("Distribuição estacionária:", stationary_distribution)
print("Estado com maior ocupação:", np.argmax(stationary_distribution))
print("Estado com menor ocupação:", np.argmin(stationary_distribution))

# Cálculo do tempo médio de recorrência do estado 0 para o estado 5 (ajuste se precisar de mais estados)
# Aqui, para uma matriz 4x4, substitua "5" por um estado válido, por exemplo, "3"
mean_recurrence_time = calculate_mean_recurrence_time(A, start_state=0, target_state=3)
print("Tempo médio de recorrência do estado 0 para o estado 3:", mean_recurrence_time)
