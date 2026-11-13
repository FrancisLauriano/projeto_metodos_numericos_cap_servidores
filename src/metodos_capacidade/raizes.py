"""Bissecao para cruzamento continuo; busca discreta para o primeiro mes inteiro."""

def bissecao(f, a, b, tolerancia_x=1e-9, tolerancia_f=1e-9, max_iter=200):
    if a >= b or tolerancia_x <= 0 or tolerancia_f <= 0 or max_iter <= 0:
        raise ValueError('Parametros invalidos')
    fa, fb = f(a), f(b)
    if fa == 0:
        return {'raiz': a, 'iteracoes': 0, 'residuo': 0.0, 'historico': []}
    if fb == 0:
        return {'raiz': b, 'iteracoes': 0, 'residuo': 0.0, 'historico': []}
    if fa * fb > 0:
        raise ValueError('Nao ha mudanca de sinal nas extremidades')
    historico = []
    for k in range(1, max_iter + 1):
        m = (a + b) / 2
        fm = f(m)
        historico.append({'iteracao': k, 'a': a, 'b': b, 'meio': m, 'residuo': abs(fm)})
        if abs(fm) < tolerancia_f and (b - a) / 2 < tolerancia_x:
            return {'raiz': m, 'iteracoes': k, 'residuo': abs(fm), 'historico': historico}
        if fa * fm <= 0:
            b, fb = m, fm
        else:
            a, fa = m, fm
    raise RuntimeError('Bissecao nao atingiu os criterios em max_iter')


def primeiro_mes_ultrapassagem(modelo, capacidade, mes_inicial, limite_meses=120):
    """Primeiro mes inteiro futuro em que demanda > capacidade (estritamente)."""
    if capacidade <= 0 or limite_meses < mes_inicial:
        raise ValueError('Capacidade ou horizonte invalido')
    for mes in range(int(mes_inicial), int(limite_meses) + 1):
        if modelo(mes) > capacidade:
            return mes
    raise ValueError('Nenhuma ultrapassagem no horizonte pesquisado')
