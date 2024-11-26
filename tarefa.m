% Define a matriz de transição
A = [
    0.1, 0.2, 0.3, 0.4;
    0.2, 0.3, 0.4, 0.1;
    0.3, 0.4, 0.2, 0.1;
    0.25, 0.25, 0.25, 0.25
];

% Cálculo da distribuição estacionária teórica usando o pacote queueing
stationary_distribution_queueing = dtmc(A);
disp("Distribuição estacionária teórica (com queueing):");
disp(stationary_distribution_queueing);

% Parâmetros de entrada para o cálculo do tempo médio de recorrência
start_state = 1;       % Estado inicial
target_state = 4;      % Estado alvo
num_recurrences = 100000; % Número de recorrências para calcular a média

% Função auxiliar para escolher o próximo estado com base nas probabilidades
function next_state = choose_next_state(probs)
    u = rand();
    cumulative_sum = cumsum(probs);
    next_state = find(u <= cumulative_sum, 1);
end

% Função para calcular o tempo médio de recorrência entre dois estados
function mean_recurrence_time = calculate_mean_recurrence_time(A, start_state, target_state, num_recurrences)
    total_steps = 0;
    recurrence_count = 0;

    while recurrence_count < num_recurrences
        state = start_state;
        steps = 0;

        % Continua até que o estado alvo seja alcançado
        while state != target_state
            state = choose_next_state(A(state, :));  % Escolhe o próximo estado
            steps += 1;
        end

        % Soma o número de passos para a próxima recorrência
        total_steps += steps;
        recurrence_count += 1;
    end

    % Calcula o tempo médio de recorrência
    mean_recurrence_time = total_steps / num_recurrences;
end

% Cálculo do tempo médio de recorrência do estado inicial para o estado alvo
mean_recurrence_time = calculate_mean_recurrence_time(A, start_state, target_state, num_recurrences);
disp(["Tempo médio de recorrência estimado (estado ", num2str(start_state), " para estado ", num2str(target_state), "):"]);
disp(mean_recurrence_time);

