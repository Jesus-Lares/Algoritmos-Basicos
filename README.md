# Algoritmos Basicos en Python
Este repositorio contiene varios algoritmos basicos hechos en python.

Cada algoritmo contiene su propio archivo README donde se explica la funcionalidad de este y como funciona.

**Nota: Este proyecto se realizo para servir como aprendizaje e investigación de los distintos algoritmos, no es usado para producción**

## Indice de los algoritmos 
Los algoritmos se dividen en ciertas campos como podrian ser los algoritmos de ordenamiento, de busqueda en un array o grafo, entre otros tipos de campos a separar. Por lo tanto, se dividiran los algoritmos según su aplicación 

### Algoritmos de busqueda 
En estos tipos de algoritmos se pueden buscar en dos tipos de datos (arreglos y grafos), por lo que se hicieron dos algoritmos por cada uno.

Para los algoritmos de busqueda en un arreglo, principalmente estan los siguientes 2:

* [Busqueda binaria.](./Searching/BinarySearch) 
* [Busqueda lineal.](./Searching/LinearSearch) 

Para los algoritmos de busqueda en un grafo, estan los siguientes 2:

* [Busqueda por profundidad.](./Searching/DepthFirstSearch) 
* [Busqueda por anchura.](./Searching/BreadthFirstSearch) 

### Algoritmos de ordenamiento
Existen distintas formas de ordenar los datos de un arreglo, claramente existen algunos que te proporcionan tener un mejor rendimiento a la hora de la busqueda, los algoritmos son los siguientes.

* [Ordenamiento burbuja (Bubble sort).](./Sorting/BubbleSort) 
* [Ordenamiento por monticulos (Heap sort).](./Sorting/HeapSort) 
* [Ordenamiento por insercion (Insertion sort).](./Sorting/InsertionSort) 
* [Ordenamiento por union (Merge sort).](./Sorting/MergeSort) 
* [Ordenamiento rapido (Quick sort).](./Sorting/QuickSort) 
* [Ordenamiento por seleccion (Selection sort).](./Sorting/SelectionSort) 

Para ver la mejora entre cada algoritmo se debe tener un arreglo con demasiados datos puesto que si el arreglo contiene menos de 1000 elementos, el rendimiento no cambia mucho.
Haciendo pruebas de esto, se ingreso un arreglo de menos de 30 elementos y uno generado por numpy de 100,000 elementos, esta prueba dio como resultado: 

#### Arreglo menor a 30 elementos
| Metodo | Tiempo (segundos)|
|--------|------------------|
| Burbuja | 6.246566772460938e-05|
| Monticulos | 6.628036499023438e-05|
| Insercion | 6.4373016357421875e-06|
| Union | 6.628036499023438e-05|
| Rapido | 4.792213439941406e-05|
| Selección | 3.7670135498046875e-05|

Siendo el mas tardado el ordenamiento por monticulos, y el mas rapido el ordenamiento por insercion.

#### Arreglo de 100,000 elementos
| Metodo | Tiempo (segundos)|
|--------|------------------|
| Burbuja | 6.6319420337677 |
| Monticulos | 0.05457925796508789 |
| Insercion | 0.0012981891632080078 |
| Union | 0.03104877471923828 |
| Rapido | 1.0856237411499023 |
| Selección | 2.321037769317627 |

Siendo el mas tardado el ordenamiento burbuja, y el mas rapido el ordenamiento por insercion.
## Como usar este repositorio
* Baja el repositorio a tu computadora.
* Ingresa al archivo que desea utilizar.
* En tu terminal corre el comando de python junto con la ubicación en donde se encuentra el archivo.