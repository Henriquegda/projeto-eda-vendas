import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# 1. Carregar os dados
# =========================
df = pd.read_csv("data/ecommerce_data.csv", encoding="latin1")

print("Primeiras linhas do dataset:")
print(df.head())

print("\nInformações gerais:")
print(df.info())

# =========================
# 2. Limpeza de dados
# =========================

# Remover linhas sem CustomerID
df = df.dropna(subset=["CustomerID"])

# Converter InvoiceDate para datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Criar coluna TotalPrice
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Remover valores negativos ou zerados
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]

# =========================
# 3. Análise Exploratória
# =========================

# Faturamento por país
revenue_country = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False)

print("\nTop 10 países por faturamento:")
print(revenue_country.head(10))

# =========================
# 4. Visualização
# =========================
plt.figure(figsize=(10, 6))
revenue_country.head(10).plot(kind="bar")
plt.title("Top 10 países por faturamento")
plt.xlabel("País")
plt.ylabel("Faturamento")
plt.tight_layout()
plt.savefig("outputs/top10_paises_faturamento.png")
plt.show()

# =========================
# 5. Insights
# =========================
print("\nINSIGHTS:")
print("1. A maior parte do faturamento vem de poucos países.")
print("2. Estratégias de marketing podem ser direcionadas aos países com maior faturamento.")
