
import numpy

def generarPoblacion(limite_inferior,limite_superior, n):
    unif = lambda xin,xsu,n : numpy.random.uniform(xin,xsu,n)
    poblacion = list( map(unif, limite_inferior,limite_superior) )
    
    return poblacion
    