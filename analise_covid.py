import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 1. Carregar os dados
df = pd.read_excel("casos_covid_brasil.xlsx")


df["Data"] = pd.to_datetime(df["Data"])

# 2. Criar pasta para gráficos
os.makedirs("graficos", exist_ok=True)


casos_regiao = df.groupby("Região")["Casos Novos"].sum().sort_values(ascending=False)
mortes_regiao = df.groupby("Região")["Mortes"].sum()
recuperados_regiao = df.groupby("Região")["Recuperados"].sum()


casos_diarios = df.groupby("Data")["Casos Novos"].sum()
mortes_diarias = df.groupby("Data")["Mortes"].sum()

# 3. Gráfico de barras – Casos por Região
plt.figure(figsize=(8,5))
sns.barplot(x=casos_regiao.index, y=casos_regiao.values, palette="Blues_d")
plt.title("Total de Casos por Região")
plt.ylabel("Casos")
plt.xlabel("Região")
plt.tight_layout()
plt.savefig("graficos/casos_por_regiao.png")
plt.close()

# 4. Gráfico de pizza – Mortes por Região
plt.figure(figsize=(6,6))
mortes_regiao.plot(kind="pie", autopct="%1.1f%%")
plt.title("Distribuição de Mortes por Região")
plt.ylabel("")
plt.tight_layout()
plt.savefig("graficos/mortes_por_regiao.png")
plt.close()

# 5. Gráfico de linha – Casos diários
plt.figure(figsize=(10,5))
casos_diarios.plot(label="Casos Novos", color="blue")
mortes_diarias.plot(label="Mortes", color="red")
plt.title("Evolução Diária – Casos e Mortes no Brasil")
plt.ylabel("Quantidade")
plt.xlabel("Data")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("graficos/evolucao_diaria.png")
plt.close()

print("\n✅ Análise concluída. Gráficos salvos na pasta 'graficos'.")
