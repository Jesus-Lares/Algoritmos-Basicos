# Ordenamiento por mezcla Python

El método de ordenamiento por mezcla (merge sort) va dividiendo el arreglo hasta que este contenga un elemento y posterior a eso inicia a juntarlos de una manera ordena.

La idea de este algoritmo es tener una función recursiva que te permita dividir el arreglo, ordenarlo y regresar el valor ordenado por lo que como primer paso se divide el arreglo a la mitad, posterior a esto, se vuelve a llamar a la recursiva pasando las dos mitades hasta que el arreglo que se envio tenga un elemento, para finalizar la función recursiva, esta manda a llamar una función de ordenamiento que su funcionamiento es el de crear un nuevo array juntando las dos mitades de una manera ordenada y retornar ese valor.
