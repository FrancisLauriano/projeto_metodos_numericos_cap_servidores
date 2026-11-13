"""Eliminacao de Gauss com pivotamento parcial (implementacao propria)."""


def eliminacao_gauss(A, b, tolerancia_pivo=1e-12):
    n = len(b)
    if n == 0 or len(A) != n or any(len(linha) != n for linha in A):
        raise ValueError('Sistema deve ser quadrado e nao vazio')
    a = [[float(valor) for valor in linha] for linha in A]
    v = [float(valor) for valor in b]
    for k in range(n):
        p = max(range(k, n), key=lambda i: abs(a[i][k]))
        if abs(a[p][k]) < tolerancia_pivo:
            raise ValueError('Sistema singular ou mal condicionado')
        a[k], a[p] = a[p], a[k]
        v[k], v[p] = v[p], v[k]
        for i in range(k + 1, n):
            fator = a[i][k] / a[k][k]
            a[i][k] = 0.0
            for j in range(k + 1, n):
                a[i][j] -= fator * a[k][j]
            v[i] -= fator * v[k]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (v[i] - sum(a[i][j] * x[j] for j in range(i + 1, n))) / a[i][i]
    return x
