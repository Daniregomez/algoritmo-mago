

def evaluarPoblacion(poblacion, fObjetivo):
    """
    Evalua la poblacion, transpone primero la matriz de poblacion y evalua cada una de las filas
    con estos resultados forma una nueva lista de tuplas con este formato (f(ind), (ind) )
    """
    return [(fObjetivo(ind), ind) for ind in zip(*poblacion)]
    