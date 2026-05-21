"""Configuracao simples para trocar IP/porta na apresentacao."""

# Troque aqui se quiser fixar outro IP para a API.
# Use "0.0.0.0" para aceitar conexoes de outras maquinas na rede.
API_HOST = "0.0.0.0"
API_PORT = 8000

# Liberado para a demo com mitmproxy. Em producao, restrinja as origens.
ALLOWED_ORIGINS = ["*"]
