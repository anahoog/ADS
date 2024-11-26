import numpy as np
import subprocess
import time

# Definição da Matriz de Transição
matriz_transicao = np.array([
    [0.7, 0.2, 0.1],  # Probabilidades de transição a partir do estado 0
    [0.3, 0.4, 0.3],  # Probabilidades de transição a partir do estado 1
    [0.2, 0.3, 0.5]   # Probabilidades de transição a partir do estado 2
])

# Configurações de Taxas de Tráfego (em Mbps)
taxas_trafego = [0, 10, 50]

# Duração de cada estado (em segundos) e total de passos
duracao_estado = 5
total_passos = 100

# Inicialização
estado_atual = 0
historico_estados = []
bytes_transmitidos = []

# Função para iniciar o tráfego com iperf
def gerar_trafego(taxa, duracao):
    if taxa == 0:  # Estado ocioso
        time.sleep(duracao)
        return 0
    else:
        # Comando iperf para gerar tráfego
        comando_iperf = [
            "iperf", "-c", "127.0.0.1", "-u", "-b", f"{taxa}M", "-t", str(duracao)
        ]
        try:
            # Captura a saída do iperf
            saida = subprocess.run(comando_iperf, capture_output=True, text=True)
            # Procura pela linha com "MBytes" para extrair transferência
            for linha in saida.stdout.splitlines():
                if "MBytes" in linha:
                    # Extração de MBytes e conversão para bytes
                    mb_transmitidos = float(linha.split()[4])  # Exemplo: 1.25
                    return mb_transmitidos * 1e6  # Converte para bytes
            return 0
        except Exception as e:
            print(f"Erro ao executar o iperf: {e}")
            return 0

# Simulação Prática
for passo in range(total_passos):
    # Registrar o estado atual
    historico_estados.append(estado_atual)
    
    # Gerar tráfego no estado atual
    trafego_gerado = gerar_trafego(taxas_trafego[estado_atual], duracao_estado)
    bytes_transmitidos.append(trafego_gerado)
    
    # Escolher próximo estado com base na matriz de transição
    estado_atual = np.random.choice([0, 1, 2], p=matriz_transicao[estado_atual])

# Proporção de tempo prático em cada estado
tempo_pratico = [historico_estados.count(i) / total_passos for i in range(3)]
vazao_media_pratica = sum(bytes_transmitidos) * 8 / (total_passos * duracao_estado * 1e6)

print("Proporção prática de tempo em cada estado:", tempo_pratico)
print("Vazão média prática (Mbps):", vazao_media_pratica)

# Análise Teórica
probs_estacionarias = np.linalg.matrix_power(matriz_transicao, 1000)[0]
vazao_media_teorica = sum(probs_estacionarias[i] * taxas_trafego[i] for i in range(3))

print("Probabilidades estacionárias (teóricas):", probs_estacionarias)
print("Vazão média teórica (Mbps):", vazao_media_teorica)
