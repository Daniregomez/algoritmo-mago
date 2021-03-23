
import numpy

def generarPoblacion(limite_inferior,limite_superior, n):
    """
    Genera poblacion de manera uniforme, una para cada variable de largo n
    cada poblacion se encuentra entre el limite_inferior y limite_superior de cada variable
    """
    return [numpy.random.uniform(limite_inferior[i] ,limite_superior[i] , n) for i in range(len(limite_inferior))]