import time
import numpy as np
import sys
from BubbleSort.main import bubbleSort
from HeapSort.main import heapSort
from InsertionSort.main import insertionSort
from MergeSort.main import mergeSort
from QuickSort.main import quickSort
from SelectionSort.main import selectionSort

sys.setrecursionlimit(100000)
sortFunctions=[
    {'name':'Bubble sort','fn':bubbleSort},
    {'name':'Heap sort','fn':heapSort},
    {'name':'Insertion sort','fn':insertionSort},
    {'name':'Merge sort','fn':mergeSort},
    {'name':'Quick sort','fn':quickSort},
    {'name':'Selection sort','fn':selectionSort}
]


def checkDelaySort(array):
    worst=None
    better=None
    nameWorst=None
    nameBetter=None

    for sort in sortFunctions:
        begin = time.time()
        orderArray = sort['fn'](array)    
        finish = time.time()
        delayTime = finish-begin
        name=sort['name']
        
        if worst==None or worst<delayTime: 
            worst,nameWorst= delayTime,name

        if better==None or better>delayTime: 
            better,nameBetter= delayTime,name

        print(f'{name} delay {delayTime} seconds') 

    return nameWorst,nameBetter

array=[97,41,99,44,45,18,68,48,69,48,32,12,10,45,15,35,2,18,68,48,69,48,32,12,10]

print(checkDelaySort(array))

np.random.seed(0)
longArray = np.random.rand(5000)
print('\nLong array')
print(checkDelaySort(longArray))