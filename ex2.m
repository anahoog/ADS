P = [0.4 0.6; 0.4 0.6];

% Vetor inicial π(0) = [1 0]
pi_0 = [1 0];
pi_10_1 = pi_0 * P^10;

% Vetor inicial π(0) = [0 1]
pi_0 = [0 1];
pi_10_2 = pi_0 * P^10;

% Vetor inicial π(0) = [0.3 0.7]
pi_0 = [0.3 0.7];
pi_10_3 = pi_0 * P^10;

% Display resultados
disp('π(10) para π(0) = [1 0]:');
disp(pi_10_1);
disp('π(10) para π(0) = [0 1]:');
disp(pi_10_2);
disp('π(10) para π(0) = [0.3 0.7]:');
disp(pi_10_3);

