"""Ejecuta las funciones de cálculo de las notas

Returns:
    Los resultados de las notas de los estudiantes.
"""
import json_manager

def corte(pc1,pc2,pp):
    """Calcula la nota definitiva de un corte

    Args:
        pc1 (int): Nota prueba corta 1
        pc2 (int): Nota prueba corta 2
        pp (int): Nota del parcial

    Returns:
        float: Nota definitiva de todo el corte
    """
    corte_total = pc1*0.05 + pc2*0.05 + pp*0.15
    return corte_total

def pruebaCorta(nota):
    """Calcula la nota equivalente de una prueba corta

    Args:
        nota (int): Nota de la prueba corta

    Returns:
        float: Nota equivalente
    """
    total = nota * 0.05
    return total

def equivalente(nota, pond):
    """Calcula la nota equivalente para una ponderación no estándar

    Args:
        nota (int): Nota de la evaluación
        pond (int): Ponderación (en %)

    Returns:
        floar: Nota equivalente
    """
    total = nota * (pond/100)
    return total

def acumulada(corte):
    data = json_manager.read_json()
    for corte in data:
        definitiva = definitiva + corte
    return