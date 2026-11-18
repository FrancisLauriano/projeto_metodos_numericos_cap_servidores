"""Pacote do projeto: ajuste por Minimos Quadrados com Eliminacao de Gauss."""
from .dados import ler_armazenamento, ler_expansoes
from .modelos import (montar_equacoes_normais, ajustar_polinomio, ajustar_quadratico,
                      avaliar_polinomio, desvios, soma_quadrados_desvios,
                      primeiro_mes_ultrapassagem)
from .sistemas import eliminacao_gauss
