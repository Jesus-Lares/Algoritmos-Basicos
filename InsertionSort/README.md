# Algoritmo de ordenamiento por inserción Python

Es un algoritmo simple de ordenamiento, eficiente sólo para ordenar arreglos pequeños. Su velocidad de procesamiento es inversamente proporcional al tamaño del arreglo: entre mayor es éste, la velocidad del algoritmo se hace cada vez más lenta. Es por ello que en sistemas complejos se prefiere utilizar algoritmos más avanzados.

La idea de este algoritmo consiste en ir recorriendo el array o matriz a partir de la posicion 1 (contando el 0), esto con la finalidad de que el primer elemento se tome como ordenado e inicie las comprobaciones desde ahi, dentro del for se tendra que recorrer el array de manera inversa hasta encontrar la posición en donde se debe encontrar el elemento, es aqui donde se hace la comprobación de si es mayor o menor dependiendo el orden y tambien sobre si la posición es mayor a 0 puesto de no ponerla seguira el ciclo ya que python no tiene inconveniente con poner array[-1], dentro del while es donde se sustiuira el valor anterior por el actual en dado de que cumpla la condición.

**En este algoritmo se agrego la funcionalidad de poner el orden en el que se desea ordenar**
