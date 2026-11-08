"""Búsqueda A* para el problema de inventario."""

from heapq import heappush, heappop
from itertools import count
from time import perf_counter

from entorno import (
    estado_inicial, es_meta, acciones, resultado, costo_accion
)
from heuristica import heuristica


def astar():
    inicio_tiempo = perf_counter()
    inicial = estado_inicial()

    # Elementos: (f, desempate, g, estado, camino)
    contador = count()
    frontera = []
    heappush(frontera, (heuristica(inicial), next(contador), 0, inicial, []))

    # Mejor costo conocido para llegar a cada estado.
    mejor_g = {inicial: 0}
    nodos_expandidos = 0

    while frontera:
        f, _, g_actual, estado, camino = heappop(frontera)

        # Descarta entradas antiguas de la cola de prioridad.
        if g_actual != mejor_g.get(estado):
            continue

        if es_meta(estado):
            return {
                "algoritmo": "A*",
                "solucion": camino,
                "estado_final": estado,
                "costo": g_actual,
                "profundidad": len(camino),
                "nodos_expandidos": nodos_expandidos,
                "tiempo_segundos": perf_counter() - inicio_tiempo,
            }

        nodos_expandidos += 1

        for accion in acciones(estado):
            sucesor = resultado(estado, accion)
            nuevo_g = g_actual + costo_accion(accion)

            if nuevo_g < mejor_g.get(sucesor, float("inf")):
                mejor_g[sucesor] = nuevo_g
                nuevo_f = nuevo_g + heuristica(sucesor)
                heappush(
                    frontera,
                    (
                        nuevo_f,
                        next(contador),
                        nuevo_g,
                        sucesor,
                        camino + [accion],
                    ),
                )

    return {
        "algoritmo": "A*",
        "solucion": None,
        "estado_final": None,
        "costo": None,
        "profundidad": None,
        "nodos_expandidos": nodos_expandidos,
        "tiempo_segundos": perf_counter() - inicio_tiempo,
    }


if __name__ == "__main__":
    print(astar())
