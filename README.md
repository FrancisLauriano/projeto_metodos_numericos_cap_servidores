<h1 align="center">Métodos Numéricos — Planejamento de Capacidade de Servidores</h1>

<p align="center">
  <img src="https://img.shields.io/static/v1?label=Python&message=3.10%2B&color=3776AB&style=for-the-badge&logo=python" alt="Python 3.10+"/>
  <img src="https://img.shields.io/static/v1?label=Jupyter&message=Notebook&color=F37626&style=for-the-badge&logo=jupyter" alt="Jupyter Notebook"/>
  <img src="https://img.shields.io/static/v1?label=Git&message=Versionamento&color=f05032&style=for-the-badge&logo=git" alt="Git"/>
  <img src="https://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=yellow&style=for-the-badge" alt="Em desenvolvimento"/>
</p>

> **Status:** :warning: Em desenvolvimento — revisar nomes da equipe, resultados e execução antes da entrega.

---

# Tópicos

:small_blue_diamond: [Contexto](#contexto-information_source)  
:small_blue_diamond: [Problema](#problema-writing_hand)  
:small_blue_diamond: [Objetivo](#objetivo-dart)  
:small_blue_diamond: [Estrutura do Projeto](#estrutura-do-projeto-file_folder)  
:small_blue_diamond: [Pré-requisitos](#pré-requisitos-warning)  
:small_blue_diamond: [Instalação](#instalação-rocket)  
:small_blue_diamond: [Como Rodar o Projeto](#como-rodar-o-projeto-computer)  
:small_blue_diamond: [Tecnologias Utilizadas](#tecnologias-utilizadas-wrench)  
:small_blue_diamond: [Documentação](#documentação-book)  
:small_blue_diamond: [Desenvolvedores](#desenvolvedores-octocat)

---

# Contexto :information_source:

<p align="justify">
Este projeto foi desenvolvido para a disciplina de <strong>Métodos Numéricos</strong>, do curso de <strong>Ciência da Computação da Universidade Católica de Pernambuco (UNICAP)</strong>, como atividade da <strong>2ª GQ</strong>. O trabalho aplica métodos numéricos à análise de dados históricos de armazenamento e ao planejamento de capacidade de servidores.
</p>

<p align="justify">
Os algoritmos numéricos foram implementados pelo grupo em um <strong>pacote Python instalável</strong>. O Jupyter Notebook importa as funções do pacote para realizar a análise, produzir gráficos e interpretar os resultados, sem conter a implementação dos métodos numéricos.
</p>

---

# Problema :writing_hand:

<p align="justify">
Uma infraestrutura de servidores registra o crescimento mensal do volume de armazenamento. Os dados históricos estão no arquivo <code>data/armazenamento.csv</code>, e as alternativas de expansão estão em <code>data/expansoes.csv</code>. A capacidade atual é de <strong>600 TB</strong>.
</p>

O problema solicita:

1. Determinar e justificar uma função matemática que represente o crescimento do armazenamento.
2. Estimar a demanda de armazenamento para o próximo mês.
3. Identificar o primeiro mês em que a demanda estimada ultrapassa 600 TB.
4. Identificar o primeiro mês em que a demanda estimada ultrapassa a capacidade de cada plano de expansão.

As capacidades totais consideradas são **700 TB (plano A)**, **800 TB (plano B)** e **900 TB (plano C)**.

---

# Objetivo :dart:

<p align="justify">
O objetivo é construir e avaliar um modelo matemático para o crescimento do armazenamento, estimar a demanda futura e determinar os meses em que diferentes limites de capacidade serão ultrapassados. A escolha dos métodos numéricos considera as necessidades específicas do problema, sem exigir a aplicação artificial de todos os métodos estudados na disciplina.
</p>

Também são discutidos os erros de ajuste, os critérios de parada dos algoritmos, a qualidade das previsões e as limitações da extrapolação.

---

# Estrutura do Projeto :file_folder:

```text
projeto_metodos_2gq/
│
├── data/
│   ├── armazenamento.csv
│   └── expansoes.csv
│
├── doc/
│   ├── Apresentacao_Capacidade_Servidores.pptx
|   ├── problema3.pdf
│   └── projetoGQ2.pdf
│
├── notebooks/
│   └── analise_capacidade.ipynb
│
├── resultados/
│   ├── ajuste_modelos.png
│   ├── limites_capacidade.png
│   ├── previsoes_capacidade.csv
│   └── residuos_ajuste.png
│
├── src/
│   └── metodos_capacidade/
│       ├── __init__.py
│       ├── dados.py
│       ├── modelos.py
│       ├── raizes.py
│       └── sistemas.py
│
├── .gitignore
├── pyproject.toml
└── README.md
```

O diretório `src/` contém os algoritmos e funções auxiliares; `notebooks/` contém a aplicação e a discussão dos resultados; `resultados/` guarda os arquivos gerados pela análise.

---

# Pré-requisitos :warning:

Antes de clonar o repositório e executar o projeto, é necessário ter instalado:

**1. Python 3.x:**
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

### 4️⃣ Ativar mbiente virtual

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
```

```bash
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


Selecione o interpretador Python do ambiente virtual e execute todas as células (**Run All**). O notebook importa o pacote `metodos_capacidade`, lê os arquivos da pasta `data/` e gera os resultados na pasta `resultados/`.

> **Atenção:** os métodos numéricos são implementados nos arquivos de `src/metodos_capacidade/`, e não nas células do notebook.

---

# Tecnologias Utilizadas :wrench:

- **Python:** implementação dos métodos e processamento dos dados.
- **Jupyter Notebook:** execução e documentação da análise.
- **Matplotlib:** visualização dos dados, ajustes e limites de capacidade.
- **pip / setuptools:** instalação do pacote Python.
- **Git e GitHub:** versionamento e publicação do projeto.

---

# Documentação :book:

A formulação matemática, as justificativas, os procedimentos e a análise estão disponíveis em:

- [Notebook — Análise de Capacidade](notebooks/analise_capacidade.ipynb)
- [Previsões em CSV](resultados/previsoes_capacidade.csv)

O notebook inclui fundamentação teórica, comparação de modelos, critérios de parada, validação temporal, discussão dos resultados, limitações, conclusão e referências.

---


# Desenvolvedores :octocat:

Time responsável pelo desenvolvimento do projeto.

| [<img src="https://github.com/Alexandre-MCS.png" width="115"><br><sub>Alexandre</sub>](https://github.com/Alexandre-MCS) | [<img src="https://github.com/Amanda-Aziz.png" width="115"><br><sub>Amanda Aziz</sub>](https://github.com/Amanda-Aziz) | [<img src="https://github.com/francisLauriano.png" width="115"><br><sub>Francis Lauriano</sub>](https://github.com/francisLauriano) | [<img src="https://github.com/lucascoffeedark.png" width="115"><br><sub>Lucas</sub>](https://github.com/lucascoffeedark) | [<img src="https://github.com/Sofiafs.png" width="115"><br><sub>Sofia Farias</sub>](https://github.com/Sofiafs) |
| :---: | :---: | :---: | :---: | :---: |

---