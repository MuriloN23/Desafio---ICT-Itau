# Trilha A - Dados & IA

## 1. Geração de Dados Sintéticos

Para simular dados de custo de nuvem, vamos gerar um dataset sintético que inclui variáveis como:
- `uso_cpu_horas`: Horas de uso da CPU
- `uso_memoria_gb`: Gigabytes de memória utilizados
- `transferencia_dados_gb`: Gigabytes de dados transferidos
- `custo_total`: Custo total (variável alvo)

Assumiremos uma relação linear simples entre o uso dos recursos e o custo, com algum ruído.

## 2. Pipeline de Ingestão e Processamento de Dados

O pipeline será composto por:
- **Ingestão**: Leitura dos dados sintéticos gerados.
- **Processamento**: Preparação dos dados para o modelo de ML (divisão em treino/teste).

## 3. Modelo de Machine Learning

Implementaremos um modelo de Regressão Linear para prever o `custo_total` com base nas variáveis de uso de recursos.

## 4. Resultados e Visualização

Serão apresentados os resultados do modelo, incluindo métricas de avaliação e um gráfico comparando os custos reais com os custos previstos.


