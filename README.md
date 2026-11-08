# Agente inteligente para optimizar inventarios de insumos tecnológicos

Proyecto académico de búsqueda en espacios de estados. Implementa BFS, DFS y A* en Python sobre un escenario determinista y discreto de inventario de memorias RAM.

## Escenario experimental

- Estado: `(día, unidades disponibles)`.
- Estado inicial: `(0, 5)`.
- Meta: alcanzar al menos 15 unidades sin superar el día 5.
- Demanda diaria: 2 unidades.
- Acción `REPOSICION`: agrega 5 unidades y luego descuenta la demanda diaria.
- Acción `ESPERA`: no agrega unidades y descuenta la demanda diaria.
- Costo de `REPOSICION`: 51 puntos (50 de reposición + 1 de operación diaria).
- Costo de `ESPERA`: 1 punto.

Los valores son hipotéticos y se utilizan exclusivamente para el experimento académico.

## Archivos

- `entorno.py`: estado, acciones, transiciones, meta y costos.
- `busqueda_bfs.py`: búsqueda en anchura.
- `busqueda_dfs.py`: búsqueda en profundidad.
- `heuristica.py`: heurística de A*.
- `busqueda_astar.py`: búsqueda A* con actualización de mejores costos.
- `main.py`: ejecuta los tres algoritmos.
- `resultados_ejecucion.txt`: ejemplo de resultados de una ejecución.

## Requisitos y ejecución

Python 3.9 o superior. No requiere librerías externas.

```bash
python main.py
```

También se puede ejecutar cada algoritmo por separado:

```bash
python busqueda_bfs.py
python busqueda_dfs.py
python busqueda_astar.py
```

## Heurística

La heurística estima el costo mínimo de las reposiciones necesarias:

`h(n) = 50 * ceil(max(0, 15 - inventario) / 3)`

Cada reposición aumenta el inventario neto en 3 unidades y su costo de compra es 50 puntos. Se omiten costos diarios, por lo que la estimación no sobrestima el costo restante y es admisible.

Esta heurística no es consistente en todos los estados debido a la acción ESPERA, que puede aumentar la estimación al reducir el inventario. Por ello A* conserva el mejor costo `g` de cada estado y permite reinsertar estados cuando se encuentra un camino más barato.

## Métricas

El programa reporta secuencia, estado final, profundidad, costo acumulado, nodos expandidos y tiempo medido con `perf_counter()`. Los tiempos varían según el equipo; para un benchmark formal se recomienda repetir ejecuciones y reportar promedio.
