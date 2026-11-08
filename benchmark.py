"""Benchmark comparativo de BFS, DFS y A*."""
import csv
import statistics
import time
from busqueda_bfs import bfs
from busqueda_dfs import dfs
from busqueda_astar import astar

ALGORITMOS = {"BFS": bfs, "DFS": dfs, "A*": astar}
REPETICIONES = 5000
CALENTAMIENTO = 100

def ejecutar_benchmark():
    resultados = []
    for nombre, algoritmo in ALGORITMOS.items():
        for _ in range(CALENTAMIENTO):
            algoritmo()
        tiempos = []
        for _ in range(REPETICIONES):
            inicio = time.perf_counter_ns()
            resultado = algoritmo()
            fin = time.perf_counter_ns()
            tiempos.append((fin - inicio) / 1_000_000)
        resultados.append({
            "Algoritmo": nombre,
            "Nodos_expandidos": resultado["nodos_expandidos"],
            "Costo": resultado["costo"],
            "Profundidad": resultado["profundidad"],
            "Promedio_ms": statistics.mean(tiempos),
            "Mediana_ms": statistics.median(tiempos),
            "Desviacion_ms": statistics.stdev(tiempos),
        })
    with open("benchmark_resultados.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=resultados[0].keys())
        escritor.writeheader()
        escritor.writerows(resultados)
    for registro in resultados:
        print(registro)

if __name__ == "__main__":
    ejecutar_benchmark()
