"""Heurística admisible para A* en el problema de inventario."""

from math import ceil
from entorno import INVENTARIO_OBJETIVO, CANTIDAD_REPOSICION, COSTO_REPOSICION


def heuristica(estado):
    """
    Estima el costo mínimo de reposiciones que faltan.

    Cada reposición aumenta el inventario neto en 3 unidades
    (5 recibidas menos 2 consumidas) y cuesta 50 puntos de compra.

    Se omiten los costos diarios, por lo que la estimación no
    sobrestima el costo real restante: es admisible.
    """
    _, inventario = estado
    deficit = max(0, INVENTARIO_OBJETIVO - inventario)
    incremento_neto = CANTIDAD_REPOSICION - 2
    reposiciones_minimas = ceil(deficit / incremento_neto)
    return reposiciones_minimas * COSTO_REPOSICION
