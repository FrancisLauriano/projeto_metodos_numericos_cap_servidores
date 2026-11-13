"""Minimos quadrados polinomiais pelas equacoes normais e eliminacao de Gauss."""
from math import sqrt
from .sistemas import eliminacao_gauss


def ajustar_polinomio(x, y, grau):
    if len(x) != len(y) or not x or grau < 0 or len(x) <= grau:
        raise ValueError('Dados insuficientes ou grau invalido')
    if len(set(x)) <= grau:
        raise ValueError('Numero insuficiente de abscissas distintas')
    # Escalonamento/centragem reduz as potencias e melhora a estabilidade numerica.
    centro = sum(x) / len(x)
    escala = max(abs(t - centro) for t in x)
    if escala == 0:
        raise ValueError('Abscissas identicas')
    z = [(t - centro) / escala for t in x]
    A = [[sum(t ** (i + j) for t in z) for j in range(grau + 1)] for i in range(grau + 1)]
    b = [sum(valor * t ** i for t, valor in zip(z, y)) for i in range(grau + 1)]
    coef = eliminacao_gauss(A, b)
    return {'grau': grau, 'coeficientes': coef, 'centro': centro, 'escala': escala}


def avaliar_polinomio(modelo, x):
    z = (x - modelo['centro']) / modelo['escala']
    valor = 0.0
    for c in reversed(modelo['coeficientes']):
        valor = valor * z + c
    return valor


def coeficientes_em_x(modelo):
    """Converte para coeficientes c0 + c1*x + ... (para exibicao)."""
    from math import comb
    c, s = modelo['centro'], modelo['escala']
    coef = [0.0] * (modelo['grau'] + 1)
    for k, ak in enumerate(modelo['coeficientes']):
        for j in range(k + 1):
            coef[j] += ak * comb(k, j) * (-c) ** (k - j) / s ** k
    return coef


def metricas_ajuste(modelo, x, y):
    pred = [avaliar_polinomio(modelo, t) for t in x]
    sq = sum((v - p) ** 2 for v, p in zip(y, pred))
    media = sum(y) / len(y)
    sst = sum((v - media) ** 2 for v in y)
    return {'sse': sq, 'rmse': sqrt(sq / len(y)), 'r2': 1 - sq / sst if sst else float('nan')}


def validacao_deixando_um_fora(x, y, grau):
    """RMSE de validacao leave-one-out: cada ponto previsto sem ser usado no ajuste."""
    erros = []
    for i in range(len(x)):
        xx = x[:i] + x[i + 1:]
        yy = y[:i] + y[i + 1:]
        m = ajustar_polinomio(xx, yy, grau)
        erros.append((avaliar_polinomio(m, x[i]) - y[i]) ** 2)
    return sqrt(sum(erros) / len(erros))
