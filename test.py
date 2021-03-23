from core.algoritmo import mago


limite_inferior = [0, 0]
limite_superior = [5, 5]
n = 10
ng = 1
fObjetivo = lambda x: x[0] + x[1] 


print(mago(limite_inferior,limite_superior, n, fObjetivo, ng))