"""Ajuste QUADRATICO por minimos quadrados; equacoes normais resolvidas por Gauss."""
from .sistemas import eliminacao_gauss


def montar_equacoes_normais(meses, volumes):
    """Retorna A e b do sistema A*[a0,a1,a2] = b."""
    if len(meses) != len(volumes) or len(meses) < 3 or len(set(meses)) < 3:
        raise ValueError("Sao necessarias pelo menos tres observacoes com meses distintos")
    n = len(meses)
    s1 = sum(meses)
    s2 = sum(m**2 for m in meses)
    s3 = sum(m**3 for m in meses)
    s4 = sum(m**4 for m in meses)
    A = [[n,s1,s2],[s1,s2,s3],[s2,s3,s4]]
    b = [sum(volumes), sum(m*y for m,y in zip(meses,volumes)),
         sum(m*m*y for m,y in zip(meses,volumes))]
    return A,b


def ajustar_quadratico(meses, volumes):
    """Calcula a0,a1,a2 do polinomio a0+a1*m+a2*m**2."""
    A,b = montar_equacoes_normais(meses,volumes)
    return eliminacao_gauss(A,b)


def avaliar_polinomio(coeficientes, mes):
    a0,a1,a2 = coeficientes
    return a0 + a1*mes + a2*mes*mes


def primeiro_mes_ultrapassagem(coeficientes, capacidade, ultimo_mes_observado, horizonte=120):
    """Verificacao direta de meses inteiros; nao usa metodo de raizes."""
    for mes in range(int(ultimo_mes_observado)+1, horizonte+1):
        valor = avaliar_polinomio(coeficientes,mes)
        if valor > capacidade:
            return mes,valor
    raise ValueError("Nao ocorreu ultrapassagem dentro do horizonte definido")
