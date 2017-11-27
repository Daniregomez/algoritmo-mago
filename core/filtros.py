
import numpy as np
from functools import reduce


def filtrarIndividuosRegion(poblacion,limite_inferion, limite_superior):
    individuosRegion=[]
    
    individuos = np.transpose(poblacion)
    
    variableCumple = lambda x,li,ls: x>=li and x<=ls
    reducirCondicion = lambda x,y: x and y    
    
    for ind in individuos:
        val = list( map(variableCumple,ind,limite_inferion, limite_superior) )
        if( reduce(reducirCondicion, val) ):
            individuosRegion.append(ind)

    return np.transpose(individuosRegion)