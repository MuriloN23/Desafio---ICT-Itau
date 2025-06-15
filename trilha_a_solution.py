import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Geração de Dados Sintéticos
def generate_synthetic_data(num_samples=1000):
    np.random.seed(42)
    uso_cpu_horas = np.random.rand(num_samples) * 1000  # 0 a 1000 horas
    uso_memoria_gb = np.random.rand(num_samples) * 500   # 0 a 500 GB
    transferencia_dados_gb = np.random.rand(num_samples) * 2000 # 0 a 2000 GB

    # Relação de custo (exemplo simplificado)
    # Custo = (CPU * 0.05) + (Memória * 0.1) + (Transferência * 0.02) + ruído
    custo_total = (uso_cpu_horas * 0.05) + \
                  (uso_memoria_gb * 0.1) + \
                  (transferencia_dados_gb * 0.02) + \
                  (np.random.randn(num_samples) * 50) # Ruído

    df = pd.DataFrame({
        'uso_cpu_horas': uso_cpu_horas,
        'uso_memoria_gb': uso_memoria_gb,
        'transferencia_dados_gb': transferencia_dados_gb,
        'custo_total': custo_total
    })
    return df

df = generate_synthetic_data()
df.to_csv('dados_custo_nuvem.csv', index=False)
print("Dados sintéticos gerados e salvos em 'dados_custo_nuvem.csv'")

# 2. Pipeline de Ingestão e Processamento de Dados
X = df[['uso_cpu_horas', 'uso_memoria_gb', 'transferencia_dados_gb']]
y = df['custo_total']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Dados divididos em conjuntos de treino e teste.")

# 3. Modelo de Machine Learning (Regressão Linear)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Modelo de Regressão Linear treinado.")

# 4. Resultados e Visualização
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")

# Salvar resultados em um CSV
results_df = pd.DataFrame({'custo_real': y_test, 'custo_previsto': y_pred})
results_df.to_csv('resultados_previsao_custo.csv', index=False)
print("Resultados da previsão salvos em 'resultados_previsao_custo.csv'")

# Gerar gráfico de comparação
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2) # Linha de 45 graus
plt.xlabel('Custo Real')
plt.ylabel('Custo Previsto')
plt.title('Custo Real vs. Custo Previsto (Regressão Linear)')
plt.grid(True)
plt.tight_layout()
plt.savefig('custo_real_vs_previsto.png')
print("Gráfico de comparação salvo como 'custo_real_vs_previsto.png'")

# Criar notebook com explicação do pipeline (simulado)
notebook_content = """
# Notebook de Análise de Custos em Nuvem com IA

Este notebook demonstra um pipeline simples de ingestão, processamento e análise de dados de custos em nuvem usando Machine Learning.

## 1. Geração de Dados Sintéticos

Geramos dados sintéticos para simular o uso de recursos (CPU, Memória, Transferência de Dados) e o custo total associado.

```python
# Código de geração de dados (ver script principal)
```

## 2. Pipeline de Ingestão e Processamento de Dados

Os dados são carregados e divididos em conjuntos de treino e teste para o treinamento do modelo.

```python
# Código de processamento de dados (ver script principal)
```

## 3. Modelo de Machine Learning

Utilizamos um modelo de Regressão Linear para prever o custo total com base no uso dos recursos.

```python
# Código de treinamento do modelo (ver script principal)
```

## 4. Resultados e Visualização

Avaliamos o desempenho do modelo usando MSE e R-squared, e visualizamos a comparação entre custos reais e previstos.

```python
# Código de avaliação e visualização (ver script principal)
```

### Gráfico de Custo Real vs. Custo Previsto

![Custo Real vs. Custo Previsto](custo_real_vs_previsto.png)

### Dados Tratados e Resultados

Os dados tratados e os resultados da previsão estão disponíveis em `dados_custo_nuvem.csv` e `resultados_previsao_custo.csv`.
"""

with open('analise_custo_nuvem.md', 'w') as f:
    f.write(notebook_content)
print("Notebook (simulado) salvo como 'analise_custo_nuvem.md'")


