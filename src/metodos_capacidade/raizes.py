

def primeiro_mes_ultrapassagem(modelo, capacidade, mes_inicial, limite_meses=120):
    """Primeiro mes inteiro futuro em que demanda > capacidade (estritamente)."""
    if capacidade <= 0 or limite_meses < mes_inicial:
        raise ValueError('Capacidade ou horizonte invalido')
    for mes in range(int(mes_inicial), int(limite_meses) + 1):
        if modelo(mes) > capacidade:
            return mes
    raise ValueError('Nenhuma ultrapassagem no horizonte pesquisado')
