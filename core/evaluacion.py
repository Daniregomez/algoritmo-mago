

def evaluarPoblacion(poblacion, fObjetivo):
    tamañoPoblacion=len(poblacion)
    numeroVariables=len(poblacion[0])
    
    resultados = []
    
    conPoblacion = 0
    while(conPoblacion < tamañoPoblacion ):
        variables = []
        
        contVariables = 0
        while(contVariables < numeroVariables):
            variables.append(poblacion[contVariables][conPoblacion])   
            contVariables+=1
        
        conPoblacion+=1
        resultados.append( (conPoblacion, fObjetivo(*variables) ) )
    
    return resultados
    