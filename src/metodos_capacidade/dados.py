"""Leitura e validacao dos arquivos fornecidos pelo professor."""
import csv
from pathlib import Path


def ler_armazenamento(caminho):
    with Path(caminho).open(newline='', encoding='utf-8-sig') as arq:
        linhas = list(csv.DictReader(arq))
    if not linhas:
        raise ValueError('Arquivo de armazenamento vazio')
    dados = [(int(l['mes']), float(l['armazenamento_tb'])) for l in linhas]
    if len({m for m, _ in dados}) != len(dados) or any(m <= 0 or y < 0 for m, y in dados):
        raise ValueError('Meses repetidos/invalidos ou volumes negativos')
    dados.sort()
    return [float(m) for m, _ in dados], [v for _, v in dados]


def ler_expansoes(caminho):
    with Path(caminho).open(newline='', encoding='utf-8-sig') as arq:
        linhas = list(csv.DictReader(arq))
    if not linhas:
        raise ValueError('Arquivo de expansoes vazio')
    planos = {l['plano'].strip(): float(l['capacidade_adicional_tb']) for l in linhas}
    if len(planos) != len(linhas) or any(not p or v < 0 for p, v in planos.items()):
        raise ValueError('Planos duplicados/invalidos ou capacidade negativa')
    return planos
