# configurações e importações
import pandas as pandas
import streamlit as streamlit_lib
import matplotlib.pyplot as matplotlib
import seaborn as seaborn



# configuração de estilo dos gráficos
seaborn.set_style('whitegrid')


# Carregamento e Limpeza dos dados
# Aplicação: necessidade de ter dados consistentes para que a analise da AMOSTRA seja confiável



## Usando @st.cache_data para que o streamlit não precise rodar e lipar os dados toda vez que interagir com o dashboard. Melhora performance.
@streamlit_lib.cache_data
def carregar_e_limpar_dados(caminho_arquivo):
    # Carrega os dados brutos
    dataFrame = pandas.read_csv(caminho_arquivo, sep=';', decimal=',')

    

    # Limpeza e padronização de texto ( variáveis qualitativas )
    # ao padronizar 'filial' e 'forma_pagamento', garantimos que a contagem de frequência destas variáveis qualitativas seja precisa.
    dataFrame['filial'] = dataFrame['filial'].str.strip().str.title()
    dataFrame['forma_pagamento'] = dataFrame['forma_pagamento'].str.strip().str.title() # str.strip retora espaços fim e início. e str.title coloca primeira letra maiúscula e o restante minúscula
    dataFrame['forma_pagamento'] = dataFrame['forma_pagamento'].replace('Credito', 'Crédito')

    # ----------------- CORREÇÃO AQUI -----------------
    # Normalizar valores da coluna de compras
    dataFrame['valor_total_compra'] = (
        dataFrame['valor_total_compra']
        .astype(str)
        .str.lower()                                 # minúsculo
        .str.replace('reais', '', regex=False)       # remove "reais"
        .str.replace('r$', '', regex=False)          # remove "R$"
        .str.replace(' ', '', regex=False)           # remove espaços
        .str.replace('.', '', regex=False)           # remove pontos de milhar
        .str.replace(',', '.', regex=False)          # troca vírgula por ponto decimal
    )

    # Converter para número
    dataFrame['valor_total_compra'] = pandas.to_numeric(
        dataFrame['valor_total_compra'], errors='coerce'
    )

    # Correção de tipos de dados ( Variáveis Quantitativas e Datas)
    # Aqui, tranformamos a coluna de texto 'valor_total_comprar' em uma Verdadeira Variável quantitativa, para poder fazer cálculos.
    dataFrame['valor_total_compra'] = pandas.to_numeric(dataFrame['valor_total_compra'], errors='coerce')
    dataFrame['data'] = pandas.to_datetime(dataFrame['data'], format='%d/%m/%Y', errors='coerce')

    # Tratamento de dados faltantes
    # Essa técnica se chama imputação
    mediana_valor = dataFrame['valor_total_compra'].median()
    dataFrame['valor_total_compra'].fillna(mediana_valor, inplace=True)
    dataFrame['forma_pagamento'].fillna('Não informado', inplace=True)

    # Tratamento Erros/ Outliers
    # Remover valores ilógicos para não distorcer as estatisticas.
    dataFrame['valor_total_compra'] = dataFrame['valor_total_compra'].abs() # abs() Retorna o valor absoluto de cada número, ou seja, todos os números negativos viram positivos

    return dataFrame


# Carega os dados usando a função carregar_e_limpar_dados()
dataFrameLimpo = carregar_e_limpar_dados('transacoes_cafeteria.csv')


# Contruir Dashboard com streamlit
# Usar dados limpos para fazer analise

streamlit_lib.set_page_config(layout="wide")

streamlit_lib.title('Análise de dados de Cafeteria')
streamlit_lib.markdown('Análise sobre a **amostra** de vendas para extrair insights sobre a **população** de clientes.')

streamlit_lib.sidebar.header('Filtros')


filial_selecionada = streamlit_lib.sidebar.multiselect(
    "Filial (Variável Qualitativa Nominal)",
    options=dataFrameLimpo['filial'].unique(),
    default=dataFrameLimpo['filial'].unique()
)

if not filial_selecionada:  # se lista estiver vazia
    dataFrameFiltrado = dataFrameLimpo.copy()
else:
    dataFrameFiltrado = dataFrameLimpo[dataFrameLimpo['filial'].isin(filial_selecionada)]


# Metricas Principais
streamlit_lib.subheader('Metricas gerais de amostra filtrada')
total_vendas = dataFrameFiltrado['valor_total_compra'].sum()
ticket_medio = dataFrameFiltrado['valor_total_compra'].mean()

col1, col2 = streamlit_lib.columns(2)
col1.metric('Total de Vendas', f'R$ {total_vendas:,.2f}')
col2.metric("Ticket Médio (Média da Var. Quantitativa)", f"R$ {ticket_medio:,.2f}")


# Gráficos
streamlit_lib.markdown('---')
streamlit_lib.subheader('Análise visual')

col_graf1, col_graf2 = streamlit_lib.columns(2)

with col_graf1:
    streamlit_lib.markdown("#### Frequência da Var. Qualitativa 'Forma de Pagamento'")
    fig, ax = matplotlib.subplots()
    dataFrameFiltrado['forma_pagamento'].value_counts().plot(kind='bar', ax=ax)
    matplotlib.xticks(rotation=45)
    streamlit_lib.pyplot(fig)
    
with col_graf2:
    streamlit_lib.markdown("#### Distribuição da Var. Quantitativa 'Valor Total da Compra'")
    fig, ax = matplotlib.subplots()
    seaborn.histplot(dataFrameFiltrado['valor_total_compra'], kde=True, ax=ax)
    streamlit_lib.pyplot(fig)

if streamlit_lib.checkbox("Mostrar tabela de dados limpos"):
    streamlit_lib.write(dataFrameFiltrado)
