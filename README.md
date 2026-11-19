<h1>Métodos Numéricos — Planejamento de Capacidade de Servidores</h1>

<p align="center">
  <img src="http://img.shields.io/static/v1?label=Python&message=3.10%2B&color=3776AB&style=for-the-badge&logo=python"/>
  <img src="http://img.shields.io/static/v1?label=Jupyter&message=Notebook&color=F37626&style=for-the-badge&logo=jupyter"/>
  <img src="http://img.shields.io/static/v1?label=Git&message=2.x&color=f05032&style=for-the-badge&logo=git"/>
  <img src="http://img.shields.io/static/v1?label=GitHub&message=2026&color=181717&style=for-the-badge&logo=github"/>
  <img src="http://img.shields.io/static/v1?label=STATUS&message=CONCLU%C3%8DDO&color=green&style=for-the-badge"/>
</p>

> Status do Projeto: :heavy_check_mark: (concluído) | :warning: (em desenvolvimento) | :x: (não iniciado)

---

# Tópicos

:small_blue_diamond: [Contexto](#contexto-information_source)

:small_blue_diamond: [Problema](#problema-writing_hand)

:small_blue_diamond: [Objetivo](#objetivo-dart)

:small_blue_diamond: [Métodos Numéricos](#métodos-numéricos-chart_with_upwards_trend)

:small_blue_diamond: [Justificativa do Grau do Polinômio](#justificativa-do-grau-do-polinômio-mag)

:small_blue_diamond: [Resultados](#resultados-bar_chart)

:small_blue_diamond: [Estrutura do Projeto](#estrutura-do-projeto-file_folder)

:small_blue_diamond: [Pré-requisitos](#pré-requisitos-warning)

:small_blue_diamond: [Instalação](#instalação-rocket)

:small_blue_diamond: [Como Rodar o Projeto](#como-rodar-o-projeto-computer)

:small_blue_diamond: [Tecnologias Utilizadas](#tecnologias-utilizadas-wrench)

:small_blue_diamond: [Documentação](#documentação-book)

:small_blue_diamond: [Referências](#referências-books)

:small_blue_diamond: [Desenvolvedores](#desenvolvedores-octocat)

---

# Contexto :information_source:

<p align="justify">
O projeto foi desenvolvido para a 2ª GQ da disciplina de <strong>Métodos Numéricos</strong>, do curso de <strong>Ciência da Computação da Universidade Católica de Pernambuco (UNICAP)</strong>. O grupo resolveu o <strong>Problema 3 — Planejamento de Capacidade de Servidores</strong>, que usa aproximação polinomial para prever a demanda de armazenamento de uma empresa.
</p>

<p align="justify">
Os métodos numéricos foram implementados pelo próprio grupo em um pacote Python, sem utilização de funções prontas. O Jupyter Notebook importa as funções do pacote e as utiliza na resolução e na análise do problema.
</p>

---

# Problema :writing_hand:

<p align="justify">
Uma empresa de armazenamento em nuvem registrou, durante 12 meses, o volume de dados armazenado pelos usuários. A capacidade atual da infraestrutura é de <strong>600 TB</strong>, e existem três planos de expansão.
</p>

**Volume armazenado** (`data/armazenamento.csv`):

| Mês | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **TB** | 137,99 | 150,45 | 172,59 | 199,09 | 219,06 | 250,06 | 292,32 | 328,07 | 366,12 | 417,17 | 464,15 | 519,14 |

**Planos de expansão** (`data/expansoes.csv`):

| Plano | Capacidade adicional | Capacidade total |
|:--:|--:|--:|
| A | 100 TB | 700 TB |
| B | 200 TB | 800 TB |
| C | 300 TB | 900 TB |

O problema pede:

- **(a)** uma função que represente o crescimento do armazenamento, com justificativa da escolha;
- **(b)** o volume estimado para o próximo mês;
- **(c)** o mês em que a demanda ultrapassa a capacidade atual de 600 TB;
- **(d)** o mês em que a demanda ultrapassa a capacidade de cada plano de expansão.

---

# Objetivo :dart:

<p align="justify">
O objetivo do trabalho é ajustar aos dados uma função que represente a tendência de crescimento do armazenamento e usá-la para estimar a demanda futura, identificando quando a capacidade atual e cada plano de expansão serão ultrapassados.
</p>

<p align="justify">
Além dos resultados, o trabalho justifica a escolha do grau do polinômio, avalia a precisão do ajuste pelos desvios e discute as limitações das previsões, que são extrapolações dos dados observados.
</p>

---

# Métodos Numéricos :chart_with_upwards_trend:

### Métodos utilizados no projeto

- **Aproximação polinomial pelo Método dos Mínimos Quadrados**: ajuste de `P(m) = a0 + a1·m + a2·m²` aos 12 meses de dados.
- **Eliminação de Gauss com pivotamento parcial**: resolução do sistema das equações normais para obter `a0`, `a1` e `a2`.

<p align="justify">
O notebook demonstra as três derivadas parciais da soma dos quadrados dos desvios, monta as equações normais e mostra a matriz, o vetor e os coeficientes explicitamente. A qualidade do ajuste é avaliada pelos desvios <code>d = y − P(m)</code> de cada mês e pela soma dos quadrados dos desvios. Para os itens (c) e (d), a função é avaliada mês a mês e comparada com cada capacidade.
</p>

> As implementações dos métodos ficam no pacote Python. O Jupyter Notebook apenas importa essas funções e as utiliza para resolver o problema.

---

# Justificativa do Grau do Polinômio :mag:

<p align="justify">
Antes de escolher o grau, o notebook calcula as primeiras diferenças (acréscimos mensais) e as segundas diferenças, apresenta uma tabela e gera o gráfico <code>resultados/analise_diferencas.png</code>.
</p>

- Os acréscimos variam, mas tendem a aumentar: o primeiro é **12,46 TB** e o último, **54,99 TB**.
- A média dos cinco primeiros acréscimos é **22,41 TB** e a dos cinco últimos, **45,36 TB**.
- As segundas diferenças **não são constantes**.

<p align="justify">
Como os acréscimos crescem, uma reta não representa os dados. Por isso, adotamos o grau 2 como hipótese simples de aproximação da tendência com curvatura, <strong>não</strong> como grau obrigatório ou matematicamente demonstrado.
</p>

---

# Resultados :bar_chart:

O notebook exibe a matriz do sistema, os **três coeficientes** e o modelo ajustado:

```text
P(m) = 125,146 + 9,929·m + 1,908·m²
```

Soma dos quadrados dos desvios: **75,60**

| Item | Resposta |
|:--|:--|
| (a) | Função quadrática ajustada por Mínimos Quadrados (acima) |
| (b) | **576,62 TB** no mês 13 |
| (c) | A capacidade atual (600 TB) é ultrapassada no **mês 14** |
| (d) | Plano A (700 TB): **mês 15**; Plano B (800 TB): **mês 17**; Plano C (900 TB): **mês 18** |

> Os meses são extrapolações do modelo e devem ser revistos com novos dados. O notebook discute a precisão e as limitações.

---

# Estrutura do Projeto :file_folder:

```text
projeto_metodos_numericos_cap_servidores/
│
├── data/
│   ├── armazenamento.csv
│   └── expansoes.csv
│
├── doc/
│   ├── problema3.pdf
│   ├── projetoGQ2.pdf
│   └── Apresentacao_Capacidade_Servidores.pptx
│
├── notebooks/
│   └── analise_capacidade.ipynb
│
├── resultados/
│   ├── ajuste_quadratico.png
│   ├── analise_diferencas.png
│   ├── desvios_ajuste.png
│   ├── limites_capacidade.png
│   └── previsoes_capacidade.csv
│
├── src/
│   └── metodos_capacidade/
│       ├── __init__.py
│       ├── dados.py
│       ├── modelos.py
│       └── sistemas.py
│
├── pyproject.toml
├── .gitignore
└── README.md
```

---

# Pré-requisitos :warning:

Antes de clonar o repositório e executar o projeto, é necessário ter instalado:

**1. Python 3.10 ou superior:**
  - Caso não tenha Python, instale: https://www.python.org/downloads/

**2. Git:**
  - Caso não tenha Git, instale: https://git-scm.com/install/

**3. VS Code (ou outra IDE com suporte a Jupyter Notebook):**
  - Caso não tenha VS Code, instale: https://code.visualstudio.com/download

---

# Instalação :rocket:

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/FrancisLauriano/projeto_metodos_numericos_cap_servidores.git
```

---

### 2️⃣ Entrar na pasta do projeto

```bash
cd projeto_metodos_numericos_cap_servidores
```

---

### 3️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

---

### 4️⃣ Ativar ambiente virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

---

### 5️⃣ Instalar o projeto e as dependências

Com o ambiente virtual ativado:

```bash
python -m pip install --upgrade pip
pip install -e .
```

O comando `pip install -e .` utiliza o arquivo `pyproject.toml` para instalar o pacote desenvolvido pelo grupo e todas as dependências necessárias ao projeto.

---

# Como Rodar o Projeto :computer:

Com o ambiente virtual ativado e o pacote instalado, execute:

```bash
jupyter notebook
```

Depois, abra:

```text
notebooks/analise_capacidade.ipynb
```

O notebook utiliza as funções implementadas no pacote localizado em:

```text
src/metodos_capacidade/
```

As implementações dos métodos numéricos estão no pacote, não dentro do notebook.

---

# Tecnologias Utilizadas :wrench:

- **Python**
- **Jupyter Notebook**
- **Matplotlib**
- **pip**
- **Git**
- **GitHub**

> O módulo **csv** pertence à biblioteca padrão do Python e, portanto, não precisa ser instalado como dependência externa.

---

# Documentação :book:

A formulação matemática, a aplicação dos métodos e a análise dos resultados estão disponíveis no notebook do projeto:

- [Análise de Capacidade de Servidores](notebooks/analise_capacidade.ipynb)
- [Apresentação em PPTX](doc/Apresentacao_Capacidade_Servidores.pptx)

O notebook apresenta:

- Leitura dos dados de armazenamento e dos planos de expansão
- Análise das primeiras e segundas diferenças
- Justificativa da escolha do grau do polinômio
- Dedução das equações normais pelo Método dos Mínimos Quadrados
- Resolução do sistema por Eliminação de Gauss com pivotamento parcial
- Desvios do ajuste e soma dos quadrados dos desvios
- Estimativa do armazenamento no mês 13
- Meses de ultrapassagem da capacidade atual e de cada plano
- Discussão das limitações

---

# Referências :books:

- RUGGIERO, M. A. G.; LOPES, V. L. R. *Cálculo Numérico: Aspectos Teóricos e Computacionais*. 2. ed. Makron Books.
- Slides da disciplina: Aula 11 (Eliminação de Gauss) e Aula 15 (Aproximação Polinomial — Mínimos Quadrados).

---

# Desenvolvedores :octocat:

Time responsável pelo desenvolvimento do projeto.

| [<img src="https://github.com/Alexandre-MCS.png" width="115"><br><sub>Alexandre</sub>](https://github.com/Alexandre-MCS) | [<img src="https://github.com/Amanda-Aziz.png" width="115"><br><sub>Amanda Aziz</sub>](https://github.com/Amanda-Aziz) | [<img src="https://github.com/francisLauriano.png" width="115"><br><sub>Francis Lauriano</sub>](https://github.com/francisLauriano) | [<img src="https://github.com/lucascoffeedark.png" width="115"><br><sub>Lucas</sub>](https://github.com/lucascoffeedark) | [<img src="https://github.com/Sofiafs.png" width="115"><br><sub>Sofia Farias</sub>](https://github.com/Sofiafs) |
| :---: | :---: | :---: | :---: | :---: |

---
