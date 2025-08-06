# 📊 Análise de COVID-19 com Excel e Gráficos

Este projeto tem como objetivo realizar uma **análise exploratória de dados da COVID-19 no Brasil** utilizando Python. Os dados incluem **casos novos, mortes e recuperações** por **data e região**, desde o início da pandemia (março de 2020) até hoje.

## 🧰 Tecnologias Utilizadas

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Openpyxl

## 📁 Estrutura do Projeto

analise_covid/
├── casos_covid_brasil.xlsx # Planilha de dados da COVID-19
├── analise_covid.py # Script com a análise e visualização
├── graficos/ # Pasta onde os gráficos são salvos
└── README.md # Documentação do projeto


## 📈 Análises Realizadas

O script realiza as seguintes análises:

- Total de **casos, mortes e recuperados** por região
- Evolução **diária** de casos e mortes em todo o Brasil
- Geração automática de **gráficos**:
  - 📊 Gráfico de barras: Casos por região
  - 🥧 Gráfico de pizza: Distribuição de mortes por região
  - 📉 Gráfico de linha: Evolução diária de casos e mortes

## 🖼️ Exemplos de Saída

Os gráficos são gerados automaticamente e salvos na pasta `graficos/`.

- `casos_por_regiao.png`
- `mortes_por_regiao.png`
- `evolucao_diaria.png`

## ▶️ Como Executar

1. Clone ou baixe o repositório.
2. Instale as dependências:

```bash
pip install pandas matplotlib seaborn openpyxl

Certifique-se de que o arquivo casos_covid_brasil.xlsx está na mesma pasta do script.
Execute:
python analise_covid.py
