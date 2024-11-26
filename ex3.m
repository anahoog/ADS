% Matriz de transição
P = [0.3 0.2 0.5; 0.1 0.8 0.1; 0.4 0.4 0.2];

% Configurando o sistema de equações lineares
A = [P' - eye(3); 1 1 1];
b = [0; 0; 0; 1];

% Resolvendo para o vetor de regime permanente
pi = A \ b;

% Exibindo o vetor de regime permanente
disp('Vetor de regime permanente:');
disp(pi);

