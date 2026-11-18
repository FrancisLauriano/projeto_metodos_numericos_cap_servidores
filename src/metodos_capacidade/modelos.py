"""Aproximacao polinomial pelo Metodo dos Minimos Quadrados.

As equacoes normais sao montadas a partir das somas dos dados e resolvidas
pela Eliminacao de Gauss implementada em ``sistemas.py``.
"""
from .sistemas import eliminacao_gauss


def montar_equacoes_normais(meses, volumes, grau=2):
    """Retorna A e b do sistema A*[a0, a1, ..., a_grau] = b.

    A[i][j] = soma(m**(i+j))  e  b[i] = soma(m**i * y).
    """
    if grau < 0:
        raise ValueError("O grau deve ser nao negativo")
    if len(meses) != len(volumes):
        raise ValueError("Meses e volumes devem ter o mesmo tamanho")
    if len(set(meses)) < grau + 1:
        raise ValueError(f"Sao necessarios pelo menos {grau + 1} meses distintos")
    potencias = [sum(m ** k for m in meses) for k in range(2 * grau + 1)]
    A = [[potencias[i + j] for j in range(grau + 1)] for i in range(grau + 1)]
    b = [sum((m ** i) * y for m, y in zip(meses, volumes)) for i in range(grau + 1)]
    return A, b


def ajustar_polinomio(meses, volumes, grau):
    """Coeficientes [a0, a1, ..., a_grau] do polinomio de Minimos Quadrados."""
    A, b = montar_equacoes_normais(meses, volumes, grau)
    return eliminacao_gauss(A, b)


def ajustar_quadratico(meses, volumes):
    """Calcula a0, a1, a2 do polinomio a0 + a1*m + a2*m**2."""
    return ajustar_polinomio(meses, volumes, 2)


def avaliar_polinomio(coeficientes, mes):
    """Avalia a0 + a1*m + ... + an*m**n."""
    return sum(a * mes ** i for i, a in enumerate(coeficientes))


def desvios(modelo, meses, volumes):
    """Desvios d_k = y_k - phi(m_k) entre o valor observado e o estimado."""
    return [y - modelo(m) for m, y in zip(meses, volumes)]


def soma_quadrados_desvios(modelo, meses, volumes):
    """F = soma de d_k**2, a quantidade minimizada pelos Minimos Quadrados."""
    return sum(d * d for d in desvios(modelo, meses, volumes))


def primeiro_mes_ultrapassagem(coeficientes, capacidade, ultimo_mes_observado, horizonte=120):
    """Primeiro mes inteiro apos o ultimo observado com P(m) > capacidade.

    Calcula P(m) mes a mes, a partir do mes seguinte ao ultimo observado,
    e para no primeiro mes em que P(m) e maior que a capacidade.
    """
    for mes in range(int(ultimo_mes_observado) + 1, horizonte + 1):
        valor = avaliar_polinomio(coeficientes, mes)
        if valor > capacidade:
            return mes, valor
    raise ValueError("Nao ocorreu ultrapassagem dentro do horizonte definido")
