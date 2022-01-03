grafo= {'a':{'b':2,'f':1},
        'b':{'a':2,'c':2,'d':2,'e':4},
        'c':{'b':2,'e':3,'z':1},
        'd':{'b':2,'e':4,'f':3},
        'e':{'b':4,'c':3,'d':4,'g':7},
        'f':{'a':1,'d':3,'g':5},
        'g':{'e':7,'f':5,'z':6},
        'z':{'c':1,'g':6}
        }

def algoritmoDijkstra(inicio,final,grafo):
    v=inicio #Valor que se ira verificando
    #Insertamos valores en la lista de valores acumulados donde a todos los valores se le insertara el numero 100 y al valor inicial un 0
    T=list(grafo)
    lista={}
    for x in T:
        lista[x]= 0 if inicio==x else 100
    #Despues del for lista={'a': 0, 'b': 100, 'c': 100, 'd': 100, 'e': 100, 'f': 100, 'g': 100, 'z': 100}

    #Se inicia un ciclo para saber el recorrido que sume un valor minimo y este terminara hasta que el vertice 
    #final deje de estar en la lista de los valores acumulados 
    while(final in T):
        #Se inicializa el for para saber cual es el minimo valor acumulado dentro de la lista de valores acumulados
        minimo=100 
        for x in T:     
            if(minimo>lista[x]):
                minimo=lista[x]
                v= x

        #Eliminamos el valor v de la lista T
        T=[x for x in T if x != v] 

        #Se busca el valor mas pequeño para la lista de valores acumulados y asi encontrar la mejor ruta por lo tanto
        #como en el for de arriba se pusieron los valores minimos lo que hace es buscar con cual nodo obtiene un menor numero
        for row in grafo[v]:   
            if lista[row]>lista[v]+grafo[v][row]:
                lista[row]=lista[v]+grafo[v][row]
                print([v,row],"\tvalor:",lista[v]+grafo[v][row])
                #([valor minimo,nodo con el que toca],sumatoria del nodo con el valor minimo mas el nodo con el que toca)

    #Se inicia a calcular la ruta empezando por el valor final hasta el inicial
    valorFinal=lista[final]#Valor acumulado del objetivo
    ruta=[final] #array para ingresar las rutas
    v=final 

    while (valorFinal>0):
        for row in grafo[v]:
            #Recorre el grafo para identificar el peso que tiene las uniones con el nodo de verificacion
            #Si el valor final menos el valor de la union con el nodo es igual al valor acumulado que tiene el nodo de la union 
            #quera decir que ese es el nodo anterior y por lo tanto pasara a ser el valor a verificar 
            if valorFinal-grafo[v][row] == lista[row]:
                valorFinal= valorFinal-grafo[v][row]
                ruta.insert(0,row)
                v=row
                break

    return ruta

inicio=input("Digite el valor inicial: ")
final=input("Digite el valor final: ")

ruta=algoritmoDijkstra(inicio,final,grafo)

print("La ruta es ",ruta, ", el tamaño de la ruta es",len(ruta)) 
