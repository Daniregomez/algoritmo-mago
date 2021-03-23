from operator import itemgetter

import numpy as np

from core.individuo import generarPoblacion
from core.evaluacion import evaluarPoblacion
from core.filtros import filtrarIndividuosRegion



def mago(limite_inferior,limite_superior, n, fObjetivo, ng):
    
    poblacion = generarPoblacion(limite_inferior,limite_superior, n)
    
    contNg = 0
    while( contNg < ng ):
        contNg+=1
        resultados = evaluarPoblacion(poblacion, fObjetivo)
        resOrdenados = ordenar(resultados)


        s = np.cov(poblacion)
        sd = np.sqrt( np.diag(s) )
        
        media = mediaPoblacion(poblacion)
        
        mini = np.subtract(media, np.multiply(0.5, sd) )
        maxi = np.add(media, np.multiply(0.5, sd) )
        
        mini1 = np.subtract(media,  sd )
        maxi1 = np.add(media,  sd )
        
        poblacionRegion_1 = filtrarIndividuosRegion(poblacion, mini, maxi)
        poblacionRegion_2 = filtrarIndividuosRegion(poblacion, mini1, maxi1)

        
        n1= len( poblacionRegion_1 ) 
        n2 = len( poblacionRegion_2 )
        n3 = n - n1 - n2
        print(n1, n2, n3)
        
        sn = np.multiply(s, 1/np.linalg.norm(s,np.inf) )
        
        grupo_mejores = seleccionarPoblacion(poblacion, resOrdenados, n1, n2)
        
        dif = calcularDiferencias(poblacion, resOrdenados, grupo_mejores, sn)
        
        grupo_mejores_mejor = np.add(grupo_mejores, dif)

    return grupo_mejores_mejor
        
    

def ordenar(resultados):
    """
    Ordena los resultados tomando la posicion 0 de los resultados 
    es decir, segun f(ind) de (f(ind), (ind) )
    """
    sorted(resultados, key=itemgetter(0))
    return resultados

def mediaPoblacion(poblacion):
    media = []
    for xi in poblacion:
        media.append( np.mean(xi) )
    
    return media

def seleccionarPoblacion(poblacion, resultadosOrdenados, n1, n2):
    """
    Funcion que toma solo los resultados de las cardinalidades n1 y n2
    posteriormente forma una lista con (ind) de resultadosOrdenados = (f(ind), (ind) )
    """
    
    filtro = resultadosOrdenados[:n2]

    individuosFiltrados = [f[1] for f in filtro]
            
    return np.transpose(np.array(individuosFiltrados))
    
    
def calcularDiferencias(poblacion, resultadosOrdenados, mejores, sn):
    individuos = np.transpose(poblacion)

    print(mejores)
    
    mejorIndividuo = mejores[0]
    
    mejoresIndividuos = np.transpose(mejores)
    
    diferencias = []
    
    for ind in mejoresIndividuos:
      dif = np.subtract( np.multiply(sn, ind), mejorIndividuo)
      diferencias.append(dif) 
    
    return np.transpose(diferencias)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    