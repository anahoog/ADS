
% Define a matriz de transição
A = [
    0.1, 0.2, 0.3, 0.4;
    0.2, 0.3, 0.4, 0.1;
    0.3, 0.4, 0.2, 0.1;
    0.25, 0.25, 0.25, 0.25
];

% Cálculo da distribuição estacionária teórica
A_powered = A^1000;  % Eleva a matriz a uma potência alta
stationary_distribution_theoretical = A_powered(1, :);  % Primeira linha representa a distribuição estacionária
disp("Distribuição estacionária teórica:");
disp(stationary_distribution_theoretical);

% Executa a simulação da distribuição estacionária
steps = 100000;
stationary_distribution_simulated = simulate_stationary_distribution(A, steps);
disp("Distribuição estacionária simulada:");
disp(stationary_distribution_simulated);

% Comparação entre a distribuição estacionária teórica e simulada
disp("Diferença entre a distribuição teórica e simulada:");
disp(stationary_distribution_theoretical - stationary_distribution_simulated);

% Cálculo do tempo médio de recorrência simulado
max_recurrences = 1000;
start_state = 1;
target_state = 4;
mean_recurrence_time_simulated = calculate_mean_recurrence_time(A, start_state, target_state, max_recurrences);
disp(["Tempo médio de recorrência simulado (estado ", num2str(start_state), " para estado ", num2str(target_state), "):"]);
disp(mean_recurrence_time_simulated);


function mean_recurrence_time = calculate_mean_recurrence_time(A, start_state, target_state, max_recurrences)
    total_recurrence_time = 0;
    recurrence_count = 0;
    state = start_state;
    steps = 0;

    while recurrence_count < max_recurrences
        state = choose_next_state(A(state, :));  % Chama a função externa
        steps += 1;

        if state == target_state
            total_recurrence_time += steps;
            recurrence_count += 1;
            steps = 0;  % Reinicia o contador de passos
        end
    end

    mean_recurrence_time = total_recurrence_time / recurrence_count;
end

function next_state = choose_next_state(probs)
    u = rand();
    cumulative_sum = cumsum(probs);
    next_state = find(u <= cumulative_sum, 1);
end

function stationary_distribution = simulate_stationary_distribution(A, steps)
    n_states = rows(A);
    state_counts = zeros(1, n_states);
    state = 1;  % Estado inicial

    for i = 1:steps
        state = choose_next_state(A(state, :));  % Chama a função externa
        state_counts(state) += 1;
    end

    stationary_distribution = state_counts / steps;
end


