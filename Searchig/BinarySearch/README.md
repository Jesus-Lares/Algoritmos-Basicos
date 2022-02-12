# Algoritmo Busqueda Binaria Python

El algoritmo de busqueda binaria es un metodo simple de busqueda de datos.

La idea de este algoritmo consiste en ir tomando el valor de la mitad del array y comprobar si este es el valor buscado, en dado caso que no sean iguales se verificara si es mayor o menor, sabiendo esto se dividira el array hasta llegar a tener un elemento con el cual se podra comprobar si es igual al valor buscado, de no ser asi se retorna un -1.

Este algoritmo es comunmente usado para arreglos que contengan mas de 100 elementos puesto que al ir partiendo el arreglo reduce el tiempo de busqueda. Una de las cosas que se pueden considerar en este algoritmo es el hecho de que se requiere una lista ordenada a diferencia de la busqueda lineal, ya que de no tener la lista ordenada el codigo fallara, puesto que al ignorar valores se puede pasar por alto el valor buscado

**Este algoritmo tiene distintas formas de aplicarse, en el codigo se pusieron dos, donde la primera tarda en concluir la busqueda en 2.9466989 segundos y la segunda tarda 2.12045836 segundos**
