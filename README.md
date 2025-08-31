# 📊 Dashboard de Análise de Vendas - Café dos Dados

![Status](https://img.shields.io/badge/status-concluído-green)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-orange)

Este projeto é um dashboard interativo construído para analisar os dados de vendas de uma rede de cafeterias fictícia, a "Café dos Dados". O objetivo é demonstrar o ciclo completo de um projeto de análise de dados, desde a limpeza e preparação de dados brutos até a criação de uma ferramenta de visualização interativa para extrair insights de negócio.

---

## 🚀 Acesso ao Dashboard

### O dashboard está publicado e pode ser acessado interativamente através do link:
### ➡️ **[https://dashboard-cafe-nks.streamlit.app/](https://dashboard-cafe-nks.streamlit.app/)**

---

## 📖 Visão Geral do Projeto

A análise parte de um conjunto de dados brutos (`.csv`) contendo 120 registros de vendas, que simula um extrato de sistema com problemas comuns do mundo real:
* Dados faltantes (nulos).
* Inconsistências na escrita (categorias duplicadas com escritas diferentes).
* Tipos de dados incorretos (valores numéricos como texto).
* Erros de registro (valores negativos).

O script em Python realiza todo o processo de **limpeza e transformação (Data Wrangling)** para, em seguida, apresentar as informações de forma clara e interativa em um dashboard construído com Streamlit.

---

## 💡 Conceitos e Habilidades Demonstradas

Este projeto foi desenvolvido para aplicar e demonstrar os seguintes conceitos fundamentais de Análise de Dados:

* **Estatística Descritiva:** Cálculo de métricas como média (ticket médio) e soma (total de vendas).
* **População vs. Amostra:** Entendimento de que a análise é feita sobre uma amostra de dados para gerar inferências sobre a população de clientes.
* **Variáveis Quantitativas e Qualitativas:** Identificação e tratamento específico para cada tipo de variável, aplicando os métodos de análise corretos.
* **Limpeza e Transformação de Dados (Data Wrangling):** Uso da biblioteca Pandas para corrigir inconsistências, tratar valores nulos e converter tipos de dados, garantindo a integridade e confiabilidade da análise.
* **Visualização de Dados:** Criação de gráficos (barras e histograma) com Matplotlib e Seaborn para comunicar os resultados de forma eficaz.
* **Desenvolvimento de Dashboard Interativo:** Utilização da biblioteca Streamlit para construir uma aplicação web que permite a filtragem e exploração dos dados pelo usuário final.
* **Boas Práticas de Desenvolvimento:** Uso de ambiente virtual (`venv`) e versionamento com Git (`.gitignore`).

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas de Análise:** Pandas
* **Bibliotecas de Visualização:** Matplotlib, Seaborn
* **Framework do Dashboard:** Streamlit
* **Ambiente de Desenvolvimento:** Visual Studio Code
* **Deploy:** Streamlit Community Cloud

---

## 🚀 Como Executar o Projeto Localmente

Para rodar este projeto na sua própria máquina, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/nikolasmarlon/portfolio-data-analytics--analise_cafe
    ```

2.  **Navegue até a pasta do projeto:**
    ```bash
    cd nome-da-pasta-do-projeto
    ```

3.  **Crie e ative um ambiente virtual:**
    ```bash
    # Criar o venv
    python -m venv venv

    # Ativar no Windows
    .\venv\Scripts\Activate.ps1

    # Ativar no macOS/Linux
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Execute a aplicação Streamlit:**
    ```bash
    streamlit run app.py
    ```
    O dashboard será aberto automaticamente no seu navegador.

---

## ✒️ Autor

* **Nikolas Marlon**
* **LinkedIn:** [Clicar aqui](www.linkedin.com/in/nikolasmarlon)
* **GitHub:** [Clique aqui](https://github.com/nikolasmarlon)