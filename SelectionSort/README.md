# Ordenamiento por selección

El método de ordenamiento por selección consiste en encontrar el menor de todos los elementos del arreglo e intercambiarlo con el que esa en la primera posición. Luego el segundo más pequeño, y así sucesivamente hasta ordenar todo el arreglo.

Lo que se hace para este algoritmo es recorrer el arreglo dando por defecto que el valor mas pequeño es la posición en la que se encuentra en el recorrido, mientras se recorre el arreglo se debe recorrer otra vez partiendo de la posicion en donde se encuentra el primer recorrido, esto con la finalidad de que se vaya comprobando si existe otro valos mas pequeño, en caso de que exista otro valor mas pequeño, la posición mas pequeña pasara a ser la del valor encontrado y una vez terminado el segundo recorrido se cambiara la posicion con la del primer recorrido.

Considero que este algoritmo es bueno para arreglos con longitud menor a 100 puesto que al recorrer dos veces el arreglo hace que lo vuelva lento ademas de realizar numerosas comparaciones.
