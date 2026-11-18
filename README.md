# Métodos Numéricos — Planejamento de Capacidade de Servidores

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)


## Contexto
Projeto da 2ª GQ de Métodos Numéricos, Ciência da Computação — UNICAP. **Problema 3:** planejar a capacidade de armazenamento a partir de 12 meses de dados.

## Problema e objetivo
A capacidade atual é **600 TB**. Os dados estão em `data/armazenamento.csv` e os planos em `data/expansoes.csv`. O projeto responde: (a) função de crescimento; (b) previsão para o mês 13; (c) primeiro mês acima de 600 TB; (d) primeiro mês acima de cada plano.

## Justificativa do grau do polinômio
Antes de escolher o grau, o notebook calcula as primeiras diferenças (acréscimos mensais) e as segundas diferenças, apresenta uma tabela e gera o gráfico `resultados/analise_diferencas.png`. Os acréscimos variam, mas tendem a aumentar: o primeiro é 12,46 TB e o último, 54,99 TB; a média dos cinco primeiros é 22,41 TB e a dos cinco últimos, 45,36 TB. As segundas diferenças **não são constantes**. Por isso, adotamos o grau 2 como hipótese simples de aproximação da tendência com curvatura, **não** como grau obrigatório ou matematicamente demonstrado. **Não há comparação com outros ajustes.**

## Métodos numéricos utilizados
**Aproximação polinomial quadrática pelo Método dos Mínimos Quadrados.** Os coeficientes `a0`, `a1` e `a2` são calculados por **Eliminação de Gauss com pivotamento parcial** sobre o sistema das equações normais. O notebook demonstra primeiro as três derivadas parciais da soma dos quadrados dos resíduos, reorganiza as equações normais e, em seguida, mostra a matriz, o vetor e os coeficientes explicitamente. Para verificar as capacidades, a função é avaliada diretamente nos meses inteiros. 

## Estrutura do projeto
```text
projeto_metodos_2gq/
├── data/
│   ├── armazenamento.csv
│   └── expansoes.csv
├── doc/
│   ├── Apresentacao_Capacidade_Servidores.pdf
│   ├── Apresentacao_Capacidade_Servidores.pptx
│   └── ROTEIRO.md
├── notebooks/
│   └── analise_capacidade.ipynb
├── resultados/
│   ├── analise_diferencas.png
│   ├── ajuste_quadratico.png
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

## Pré-requisitos
Python 3.10+, Git (para clonar o repositório) e VS Code com extensão Jupyter ou Jupyter Notebook.

## Instalação
Na pasta raiz do projeto:
```bash
python -m venv .venv
```
Ative o ambiente no Windows com `.venv\Scripts\activate` ou no Linux/macOS com `source .venv/bin/activate`.
```bash
python -m pip install -e ".[notebook]"
```

## Como executar
Abra `notebooks/analise_capacidade.ipynb` no VS Code e selecione o ambiente Python instalado. Execute as células na ordem. Alternativamente, na raiz, execute `jupyter notebook` e abra o mesmo arquivo.

## Resultados
O notebook exibe a matriz do sistema, os **três coeficientes** e o modelo `P(m) = a0 + a1*m + a2*m²`. Estima **576,62 TB** no mês 13 e prevê ultrapassagens em **14 (600 TB)**, **15 (700 TB)**, **17 (800 TB)** e **18 (900 TB)**.

## Documentação
- [Notebook e justificativas](notebooks/analise_capacidade.ipynb)
- [Apresentação em PDF](doc/Apresentacao_Capacidade_Servidores.pdf)
- [Roteiro de apresentação](doc/ROTEIRO.md)

## Referências
- RUGGIERO, M. A. G.; LOPES, V. L. R. *Cálculo Numérico: Aspectos Teóricos e Computacionais*. 2. ed. Makron Books.
- Slides da disciplina: Aula 11 (Eliminação de Gauss) e Aula 15 (Aproximação Polinomial — Mínimos Quadrados).

## Desenvolvedores
Time responsável pelo desenvolvimento do projeto.

| [<img src="https://github.com/Alexandre-MCS.png" width="115"><br><sub>Alexandre</sub>](https://github.com/Alexandre-MCS) | [<img src="https://github.com/Amanda-Aziz.png" width="115"><br><sub>Amanda Aziz</sub>](https://github.com/Amanda-Aziz) | [<img src="https://github.com/francisLauriano.png" width="115"><br><sub>Francis Lauriano</sub>](https://github.com/francisLauriano) | [<img src="https://github.com/lucascoffeedark.png" width="115"><br><sub>Lucas</sub>](https://github.com/lucascoffeedark) | [<img src="https://github.com/Sofiafs.png" width="115"><br><sub>Sofia Farias</sub>](https://github.com/Sofiafs) |
| :---: | :---: | :---: | :---: | :---: |

