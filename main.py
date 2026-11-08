"""Ejecuta BFS, DFS y A* sobre el mismo problema de inventario."""

from busqueda_bfs import bfs
from busqueda_dfs import dfs
from busqueda_astar import astar


def mostrar_resultado(resultado):
    print(f"\n--- {resultado['algoritmo']} ---")
    print("Secuencia:", resultado["solucion"])
    print("Estado final:", resultado["estado_final"])
    print("Profundidad:", resultado["profundidad"])
    print("Costo total:", resultado["costo"])
    print("Nodos expandidos:", resultado["nodos_expandidos"])
    print(f"Tiempo: {resultado['tiempo_segundos']:.8f} segundos")


if __name__ == "__main__":
    print("PROYECTO: AGENTE INTELIGENTE PARA OPTIMIZAR INVENTARIOS")
    mostrar_resultado(bfs())
    mostrar_resultado(dfs())
    mostrar_resultado(astar())
