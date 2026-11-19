# Métodos Numéricos — Planejamento de Capacidade de Servidores

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)


## Contexto
Projeto da 2ª GQ de Métodos Numéricos, Ciência da Computação — UNICAP. **Problema 3:** planejar a capacidade de armazenamento a partir de 12 meses de dados.

## Problema e objetivo
A capacidade atual é **600 TB**. Os dados estão em `data/armazenamento.csv` e os planos em `data/expansoes.csv`. O projeto responde: (a) função de crescimento; (b) previsão para o mês 13; (c) primeiro mês acima de 600 TB; (d) primeiro mês acima de cada plano.

## Justificativa do grau do polinômio
Antes de escolher o grau, o notebook calcula as primeiras diferenças (acréscimos mensais) e as segundas diferenças, apresenta uma tabela e gera o gráfico `resultados/analise_diferencas.png`. Os acréscimos variam, mas tendem a aumentar: o primeiro é 12,46 TB e o último, 54,99 TB; a média dos cinco primeiros é 22,41 TB e a dos cinco últimos, 45,36 TB. As segundas diferenças **não são constantes**. Por isso, adotamos o grau 2 como hipótese simples de aproximação da tendência com curvatura, **não** como grau obrigatório ou matematicamente demonstrado.

## Métodos numéricos utilizados
**Aproximação polinomial quadrática pelo Método dos Mínimos Quadrados.** Os coeficientes `a0`, `a1` e `a2` são calculados por **Eliminação de Gauss com pivotamento parcial** sobre o sistema das equações normais. O notebook demonstra primeiro as três derivadas parciais da soma dos quadrados dos desvios, reorganiza as equações normais e, em seguida, mostra a matriz, o vetor e os coeficientes explicitamente. A qualidade do ajuste é avaliada pelos desvios `d = y − P(m)` de cada mês e pela soma dos quadrados dos desvios (`resultados/desvios_ajuste.png`). Para verificar as capacidades, a função é avaliada diretamente nos meses inteiros.

## Estrutura do projeto
```text
projeto_metodos_numericos_cap_servidores/
├── data/
│   ├── armazenamento.csv
│   └── expansoes.csv
├── doc/
│   ├── problema3.pdf
│   ├── projetoGQ2.pdf
│   └── Apresentacao_Capacidade_Servidores.pptx
├── notebooks/
│   └── analise_capacidade.ipynb
├── resultados/
│   ├── ajuste_quadratico.png
│   ├── analise_diferencas.png
│   ├── desvios_ajuste.png
│   ├── limites_capacidade.png
│   └── previsoes_capacidade.csv
├── src/metodos_capacidade/
│   ├── __init__.py
│   ├── dados.py
│   ├── modelos.py
│   └── sistemas.py
├── pyproject.toml
├── .gitignore
└── README.md
```

---

## Pré-requisitos :warning:

Antes de clonar o repositório e executar o projeto, é necessário ter instalado:

**1. Python 3.x:**
  - Caso não tenha Python, instale: https://www.python.org/downloads/

**2. Git:**
  - Caso não tenha Git, instale: https://git-scm.com/install/

**3. VS Code (ou outra IDE com suporte a Jupyter Notebook):**
  - Caso não tenha VS Code, instale: https://code.visualstudio.com/download

---

## Instalação :rocket:

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
```

```bash
pip install -e .
```

O comando `pip install -e .` utiliza o arquivo `pyproject.toml` para instalar o pacote desenvolvido pelo grupo e todas as dependências necessárias ao projeto. 

---

## Como Rodar o Projeto :computer:

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

## Tecnologias Utilizadas :wrench:

- **Python**
- **Jupyter Notebook**
- **Matplotlib**
- **pip**
- **Git**
- **GitHub**

## Resultados
O notebook exibe a matriz do sistema, os **três coeficientes** e o modelo ajustado:

`P(m) = 125,146 + 9,929·m + 1,908·m²`  (soma dos quadrados dos desvios = 75,60)

| Item | Resposta |
|:--|:--|
| (a) | Função quadrática ajustada por Mínimos Quadrados (acima) |
| (b) | **576,62 TB** no mês 13 |
| (c) | A capacidade atual (600 TB) é ultrapassada no **mês 14** |
| (d) | Plano A (700 TB): **mês 15**; Plano B (800 TB): **mês 17**; Plano C (900 TB): **mês 18** |

Os meses são extrapolações do modelo e devem ser revistos com novos dados; o notebook discute a precisão e as limitações.

## Documentação
- [Notebook e justificativas](notebooks/analise_capacidade.ipynb)
- [Apresentação em PPTX](doc/Apresentacao_Capacidade_Servidores.pptx)
  

## Referências
- RUGGIERO, M. A. G.; LOPES, V. L. R. *Cálculo Numérico: Aspectos Teóricos e Computacionais*. 2. ed. Makron Books.
- Slides da disciplina: Aula 11 (Eliminação de Gauss) e Aula 15 (Aproximação Polinomial — Mínimos Quadrados).

## Desenvolvedores
Time responsável pelo desenvolvimento do projeto.

| [<img src="https://github.com/Alexandre-MCS.png" width="115"><br><sub>Alexandre</sub>](https://github.com/Alexandre-MCS) | [<img src="https://github.com/Amanda-Aziz.png" width="115"><br><sub>Amanda Aziz</sub>](https://github.com/Amanda-Aziz) | [<img src="https://github.com/francisLauriano.png" width="115"><br><sub>Francis Lauriano</sub>](https://github.com/francisLauriano) | [<img src="https://github.com/lucascoffeedark.png" width="115"><br><sub>Lucas</sub>](https://github.com/lucascoffeedark) | [<img src="https://github.com/Sofiafs.png" width="115"><br><sub>Sofia Farias</sub>](https://github.com/Sofiafs) |
| :---: | :---: | :---: | :---: | :---: |

