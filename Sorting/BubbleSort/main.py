
def bubbleSort(array):
    desorder = True
    while desorder:
        desorder=False
        for index in range(len(array)-1):
            if array[index] > array[index+1]:
                array[index],array[index+1]=array[index+1],array[index]
                desorder=True
    return array

""" 
array=[97,41,99,44,45,18,68,48,69,48,32,12,10]
print(bubbleSort(array)) 
"""