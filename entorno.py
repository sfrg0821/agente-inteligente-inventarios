"""Entorno determinista para la gestión de inventario de memorias RAM."""

from typing import List, Tuple

Estado = Tuple[int, int]  # (día, unidades disponibles)

DIA_MAXIMO = 5
INVENTARIO_INICIAL = 5
INVENTARIO_OBJETIVO = 15
DEMANDA_DIARIA = 2
CANTIDAD_REPOSICION = 5
COSTO_REPOSICION = 50
COSTO_OPERACION_DIARIA = 1

ESPERA = "ESPERA"
REPOSICION = "REPOSICION"


def estado_inicial() -> Estado:
    """Devuelve el estado inicial del problema."""
    return (0, INVENTARIO_INICIAL)


def es_meta(estado: Estado) -> bool:
    """La meta se alcanza con 15 o más unidades dentro del horizonte."""
    dia, inventario = estado
    return inventario >= INVENTARIO_OBJETIVO and dia <= DIA_MAXIMO


def acciones(estado: Estado) -> List[str]:
    """Devuelve las acciones válidas desde un estado."""
    dia, inventario = estado

    if dia >= DIA_MAXIMO or es_meta(estado):
        return []

    posibles = []
    # Cada acción representa un día: se aplica la decisión y luego la demanda.
    inventario_espera = inventario - DEMANDA_DIARIA
    if inventario_espera >= 0:
        posibles.append(ESPERA)

    inventario_reposicion = (
        inventario + CANTIDAD_REPOSICION - DEMANDA_DIARIA
    )
    if inventario_reposicion >= 0:
        posibles.append(REPOSICION)

    return posibles


def resultado(estado: Estado, accion: str) -> Estado:
    """Aplica una acción y devuelve el estado sucesor."""
    if accion not in acciones(estado):
        raise ValueError(f"Acción no válida: {accion}")

    dia, inventario = estado

    if accion == REPOSICION:
        nuevo_inventario = (
            inventario + CANTIDAD_REPOSICION - DEMANDA_DIARIA
        )
    elif accion == ESPERA:
        nuevo_inventario = inventario - DEMANDA_DIARIA
    else:
        raise ValueError(f"Acción desconocida: {accion}")

    return (dia + 1, nuevo_inventario)


def costo_accion(accion: str) -> int:
    """Costo económico simplificado de una acción."""
    if accion == REPOSICION:
        return COSTO_REPOSICION + COSTO_OPERACION_DIARIA
    if accion == ESPERA:
        return COSTO_OPERACION_DIARIA
    raise ValueError(f"Acción desconocida: {accion}")


def costo_camino(camino: List[str]) -> int:
    """Calcula el costo acumulado de una secuencia de acciones."""
    return sum(costo_accion(a) for a in camino)
