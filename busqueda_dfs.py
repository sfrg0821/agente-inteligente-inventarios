"""Búsqueda en profundidad (DFS) para el problema de inventario."""

from time import perf_counter
from entorno import estado_inicial, es_meta, acciones, resultado, costo_camino


def dfs():
    inicio_tiempo = perf_counter()
    inicial = estado_inicial()

    frontera = [(inicial, [])]  # La lista se utiliza como pila LIFO.
    visitados = {inicial}
    nodos_expandidos = 0

    while frontera:
        estado, camino = frontera.pop()

        if es_meta(estado):
            return {
                "algoritmo": "DFS",
                "solucion": camino,
                "estado_final": estado,
                "costo": costo_camino(camino),
                "profundidad": len(camino),
                "nodos_expandidos": nodos_expandidos,
                "tiempo_segundos": perf_counter() - inicio_tiempo,
            }

        nodos_expandidos += 1

        # Se insertan en orden inverso para explorar primero ESPERA,
        # manteniendo el mismo orden lógico de acciones que BFS.
        for accion in reversed(acciones(estado)):
            sucesor = resultado(estado, accion)
            if sucesor not in visitados:
                visitados.add(sucesor)
                frontera.append((sucesor, camino + [accion]))

    return {
        "algoritmo": "DFS",
        "solucion": None,
        "estado_final": None,
        "costo": None,
        "profundidad": None,
        "nodos_expandidos": nodos_expandidos,
        "tiempo_segundos": perf_counter() - inicio_tiempo,
    }


if __name__ == "__main__":
    print(dfs())
