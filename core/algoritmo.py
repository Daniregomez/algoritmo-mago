import numpy as np

import individuo.generarPoblacion
import evaluacion.evaluarPoblacion
import filtros.filtrarIndividuosRegion


def mago(limite_inferior,limite_superior, n, fObjetivo, ng):
    
    poblacion = generarPoblacion(limite_inferior,limite_superior, n)
    
    contNg = 0
    while( contNg < ng ):
        contNg+=1
        resultados = evaluarPoblacion(poblacion, fObjetivo)
        resOredenados = ordenar(resultados)
        
        s = np.cov(poblacion)
        sd = np.sqrt( np.diag(s) )
        
        media = mediaPoblacion(poblacion)
        
        mini = np.subtract(media, np.multiply(0.5, sd) )
        maxi = np.add(media, np.multiply(0.5, sd) )
        
        mini1 = np.subtract(media,  sd )
        maxi1 = np.add(media,  sd )
        
        poblacionRegion_1 = filtrarIndividuosRegion(poblacion, mini, maxi)
        poblacionRegion_2 = filtrarIndividuosRegion(poblacion, mini1, maxi1)
        
        tamannoRegion_1 = len( poblacionRegion_1[0] )
        tamannoRegion_2 = len( poblacionRegion_2[0] )
        tamannoRegion_3 = len( poblacion[0] ) - tamannoRegion_1 - tamannoRegion_2 -1
        
        sn = np.multiply(s, 1/np.linalg.norm(s,np.inf) )
        
        grupo_mejores = seleccionarPoblacion(poblacion, 1, tamannoRegion_1)
        
        dif = calcularDiferencias(poblacion, resOredenados, grupo_mejores, sn)
        
        grupo_mejores_mejor = np.add(grupo_mejores, dif)
        
    

def ordenar(resultados):
    return sorted(resultados, key=lambda tup: tup[1] )

def mediaPoblacion(poblacion):
    media = []
    for xi in poblacion:
        media.append( np.men(xi) )
    
    return media

def seleccionarPoblacion(poblacion, resultadosOrdenados, n0, n1):
    individuos = np.transpose(poblacion)
    
    filtro = resultadosOrdenados[n0:n1]
    
    individuosFiltrados = []
    
    for f in filtro:
        individuosFiltrados.append( individuos[ f[0] ] )
        
    return np.transpose(individuosFiltrados)
    
    
def calcularDiferencias(poblacion, resultadosOrdenados, mejores, sn):
    individuos = np.transpose(poblacion)
    
    indiceMejor = resultadosOrdenados[0][0]
    mejorIndividuo = individuos[indiceMejor]
    
    mejoresIndividuos = np.transpose(mejores)
    
    diferencias = []
    
    for ind in mejoresIndividuos:
      dif = np.subtract( np.multiply(sn, ind), mejorIndividuo)
      diferencias.append(dif) 
    
    return np.transpose(diferencias)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    