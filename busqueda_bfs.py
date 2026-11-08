"""Búsqueda en anchura (BFS) para el problema de inventario."""

from collections import deque
from time import perf_counter
from entorno import estado_inicial, es_meta, acciones, resultado, costo_camino


def bfs():
    inicio_tiempo = perf_counter()
    inicial = estado_inicial()

    frontera = deque([(inicial, [])])
    visitados = {inicial}
    nodos_expandidos = 0

    while frontera:
        estado, camino = frontera.popleft()

        if es_meta(estado):
            return {
                "algoritmo": "BFS",
                "solucion": camino,
                "estado_final": estado,
                "costo": costo_camino(camino),
                "profundidad": len(camino),
                "nodos_expandidos": nodos_expandidos,
                "tiempo_segundos": perf_counter() - inicio_tiempo,
            }

        nodos_expandidos += 1

        for accion in acciones(estado):
            sucesor = resultado(estado, accion)
            if sucesor not in visitados:
                visitados.add(sucesor)
                frontera.append((sucesor, camino + [accion]))

    return {
        "algoritmo": "BFS",
        "solucion": None,
        "estado_final": None,
        "costo": None,
        "profundidad": None,
        "nodos_expandidos": nodos_expandidos,
        "tiempo_segundos": perf_counter() - inicio_tiempo,
    }


if __name__ == "__main__":
    print(bfs())
