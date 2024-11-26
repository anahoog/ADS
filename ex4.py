import numpy as np

# Matriz de transição
A = np.array([[0.1, 0.2, 0.3, 0.4], 
              [0.2, 0.3, 0.4, 0.1],
              [0.3, 0.4, 0.2, 0.1],
              [0.25, 0.25, 0.25, 0.25]])

# Função para simular uma movimentação em uma cadeia de Markov
def markov_move(A, s):
    probs = A[s]  # Pegamos a linha da matriz de transição referente ao estado atual
    u = np.random.uniform(0, 1)
    accum = 0
    for n, prob in enumerate(probs):
        accum += prob
        if u <= accum:
            return n
    return len(probs) - 1  # Retorna o último estado se não encontrado antes

# Estado inicial
s = 0

# Simulação da cadeia de Markov para 10 passos
for i in range(10):
    s = markov_move(A, s)
    print(f"Passo {i + 1}: Estado atual = {s}")
