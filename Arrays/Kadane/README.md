# Algoritmo Kadane Python

El algoritmo de Kadane creado por Joseph Born Kadane, es un algoritmo de programacion dinámica iterativa que se ejecuta en tiempo lineal (el numero de operaciones depende directamente del tamaño del problema) para el calculo de la suma maxima en un array cuyo último índice sea la posición en la que nos encontramos.

La idea de este algoritmo consiste en ir recorriendo el array o matriz e ir encontrando un conjunto de numeros consecutivos en la matriz que te de la suma maxima que se pueda encontrar dentro del array.
Por ejemplo: si se tiene el array [-3, -4, 5, -1, 2, -4, 6]. Al sumar todos su elementos obtienes un 1 como sumatoria pero si solo agarras el conjunto [5, -1, 2, -4, 6] obtienes un 8, este problema se soluciona con 2 logicas distintas.

1. Recorrer 2 veces el array haciendo que el algoritmo se vuelva cuadratico, donde en el primer ciclo tengamos el indice en el que nos encontramos para hallar en donde empieza la sumatoria maxima y el segundo ciclo que ira sumando todo desde el indice que te proporcina el primer ciclo hasta donde termina el array, el valor maximo se sobrescribira en dado caso de encontrar un valor mas alto al antes estipulado.
2. Recorrer el array una vez haciendo que el algoritmo se vuela lineal, esta logica de hacerlo hace que recorra el array sumando siempre el valor que tiene la posicion, al encontrar un numero mayor este se le otorgara al valor maximo, en dado caso que la sumatoria sea menor a cero, el valor que lleva la sumatoria pasara a ser cero por lo que empezara la nueva sumatoria en este punto.

**En este algoritmo se modifico para que retornara el arreglo de la sumatoria y el valor maximo**
