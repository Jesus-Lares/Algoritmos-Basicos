# Ordenamiento por monticulos (Heapsort)

Este algoritmo de ordenamiento requiere ciertos conocimientos acerca de dos tipos de estructura de datos (arrays,arboles-grafos). Para poder hacer el ordenamiento es necesario primero generar la estructura Heap o monticulo (arbol binario completo que permite implementar una cola con prioridades, donde los elementos se almacenan cumpliendo la propiedad que se le impone la cual normalmente es que el nodo padre siempre tendra un valor mas alto al nodo hijo).

El algoritmo consiste en remover el mayor elemento que es siempre es la raiz, para esto se debe generar la estructura Heap donde este te deja como nodo raiz el valor mas grande y posterior a eso lo elimina de la raiz y lo posiciona al final, finalmente decrementa la cantidad de elementos del Heap y vuelve a repetir los pasos.

Para generar la estrucura se debe usar la propiedad de los arboles binarios para encontrar los hijos y los padres de cualquier nodo. Esta te dice que si tu elemento tiene un indice "i", el nodo hijo de la izquierda tendra un indice "2i+1" y el de la derecha sera "2i+2", para encontrar un padre se utiliza "(i-1)/2". Por lo tanto, si el indice es la posicion 2 del arreglo, los nodos quedarian asi:

- Nodo en la posicion "2"
- Nodo hijo de la izquierda "2\*2 + 1=5"
- Nodo hijo de la derecha "2\*2 + 2=6"
- Nodo padre "(2-1) / 2 =.5 = 0"

**Entender como se posicionan los nodos es importante para entender este algoritmo**

La idea de implementación es sencilla, primero se debe encontrar el valor mas grande, se inicia por recorrer el arreglo a partir de la mitad hacia la posicion inicial ya que con esto es suficente para ver los valores de los nodos hijos por lo que el valor recorrido se enviara a una funcion la cual recibe 3 parametros(arreglo,longitud del arreglo, nodo que se va a verificar), con estos parametros se genera el arbol binario donde al inico encuentra sus nodos hijos, posterior a esto verifica que los nodos hijos existan en el arreglo y si es mayor al nodo padre, de ser asi los cambiara y mandara a llamar nuevamente a la función pero ahora con el nodo hijo como padre, de lo contrario la función terminara.
Una vez que termine el recorrido se debera tener el valor mas grande en la posición inicial, teniendo esto, se recorrera nuevamente el arreglo pero ahora de la posicion final menos uno hasta la posición inicial, el valor inicial se sustituira por el valor final y se volvera a llamar a la función para crear la estructura mandando el arreglo, la posición del recorrido y la posición inicial para que se tome como nodo padre.
