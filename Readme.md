# Desafio de Projeto P&D Multicloud com IA - Trilha A

Este repositório contém a solução desenvolvida para a **Trilha A – Dados & IA** do desafio de Projeto P&D Multicloud com IA. O objetivo desta trilha é criar um pipeline simples de ingestão e processamento de dados, a partir de dados públicos de custo de nuvem, e implementar um modelo de machine learning para prever custos ou identificar padrões de uso.

## Estrutura do Repositório

- `trilha_a_solution.py`: Script Python contendo a implementação do pipeline de dados e o modelo de Machine Learning.
- `analise_custo_nuvem.md`: Um "notebook" em formato Markdown explicando o pipeline, o modelo e os resultados.
- `custo_real_vs_previsto.png`: Gráfico gerado pelo modelo, comparando os custos reais com os custos previstos.
- `dados_custo_nuvem.csv`: Arquivo CSV com os dados sintéticos gerados e tratados.
- `resultados_previsao_custo.csv`: Arquivo CSV com os resultados da previsão do modelo.
- `trilha_a_overview.md`: Visão geral da solução proposta para a Trilha A.

## Como Executar

Para executar a solução, siga os passos abaixo:

### Pré-requisitos

Certifique-se de ter o Python 3 instalado em seu ambiente. As bibliotecas necessárias podem ser instaladas via `pip`:

```bash
pip install scikit-learn matplotlib seaborn pandas numpy
```

### Execução do Script

Navegue até o diretório raiz do projeto e execute o script Python:

```bash
python trilha_a_solution.py
```

Este script irá:
1. Gerar dados sintéticos de custo de nuvem e salvá-los em `dados_custo_nuvem.csv`.
2. Treinar um modelo de Regressão Linear para prever custos.
3. Salvar os resultados da previsão em `resultados_previsao_custo.csv`.
4. Gerar um gráfico de comparação entre custos reais e previstos, salvando-o como `custo_real_vs_previsto.png`.
5. Criar um arquivo Markdown (`analise_custo_nuvem.md`) que simula um notebook, explicando o processo.

## Detalhes da Solução - Trilha A

### 1. Geração de Dados Sintéticos

Para simular dados de custo de nuvem, foi gerado um dataset sintético com 1000 amostras, incluindo as seguintes variáveis:
- `uso_cpu_horas`: Horas de uso da CPU (valores aleatórios entre 0 e 1000).
- `uso_memoria_gb`: Gigabytes de memória utilizados (valores aleatórios entre 0 e 500).
- `transferencia_dados_gb`: Gigabytes de dados transferidos (valores aleatórios entre 0 e 2000).
- `custo_total`: Custo total, calculado com base em uma relação linear simples entre o uso dos recursos e um ruído aleatório.

### 2. Pipeline de Ingestão e Processamento de Dados

O pipeline de dados é simples e direto:
- **Ingestão**: Os dados sintéticos são lidos a partir do DataFrame gerado.
- **Processamento**: Os dados são divididos em conjuntos de treino (80%) e teste (20%) usando `train_test_split` do `scikit-learn`, preparando-os para o treinamento e avaliação do modelo de Machine Learning.

### 3. Modelo de Machine Learning

Foi implementado um modelo de **Regressão Linear** para prever o `custo_total` com base nas variáveis de uso de recursos (`uso_cpu_horas`, `uso_memoria_gb`, `transferencia_dados_gb`). A escolha da Regressão Linear se deu pela simplicidade e interpretabilidade, adequada para um protótipo inicial.

### 4. Resultados e Visualização

Após o treinamento do modelo, foram calculadas as seguintes métricas de avaliação:
- **Mean Squared Error (MSE)**: Mede a média dos quadrados dos erros, indicando a magnitude dos erros de previsão.
- **R-squared (R2)**: Representa a proporção da variância na variável dependente que é previsível a partir das variáveis independentes. Um valor mais próximo de 1 indica um melhor ajuste do modelo.

Um gráfico de dispersão (`custo_real_vs_previsto.png`) foi gerado para visualizar a relação entre os custos reais e os custos previstos pelo modelo. Uma linha de 45 graus é plotada para facilitar a comparação visual: pontos próximos a essa linha indicam previsões mais precisas.

## Considerações Finais

Esta solução demonstra um protótipo funcional para a Trilha A, abordando a ingestão de dados sintéticos, o processamento e a aplicação de um modelo de Machine Learning para previsão de custos. Para um cenário real, a ingestão de dados envolveria APIs de provedores de nuvem e a complexidade do modelo de ML poderia ser aumentada para capturar relações mais complexas nos dados.
