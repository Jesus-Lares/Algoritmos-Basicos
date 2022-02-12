# Ordenamiento rapido Python

El método de ordenamiento rapido (quicksort) va de la mano con la frase divide y venceras puesto que este algoritmo va dividiendo el arreglo hasta que este contenga un elemento.

Lo que se hace para este algoritmo es elegir un pivote el cual sera utilizado para dividir el arreglo con la condición si es mayor o menor (en el codigo tambien se ingreso la condición de igual con el fin de hacer mas eficiente el codigo), posterior a dividir el arreglo se retorna la función con el arreglo menor + el pivote (en este caso es un arreglo de los valores iguales al pivote) + la función con el arreglo mayor. Esta función recursiva continuara hasta que la longitud del arreglo mandado sea igual o menor a 1, de ser asi se retorna el arreglo que llego como parametro.

Este algoritmo es bastante bueno, su defecto parte de la elección del pivote, esta elección se puede hacer de distintas maneras como lo seria el escoger el primero, el ultimo, el valor del medio o la mediana de 3 numeros.
