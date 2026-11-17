"""Pacote do projeto: ajuste quadratico por minimos quadrados e Gauss."""
from .dados import ler_armazenamento, ler_expansoes
from .modelos import (montar_equacoes_normais, ajustar_quadratico,
                      avaliar_polinomio, primeiro_mes_ultrapassagem)
from .sistemas import eliminacao_gauss
