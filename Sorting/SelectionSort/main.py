
def selectionSort(array):
    
    for i in range(len(array)):
        min_value=i
        
        for j in range(i+1,len(array)):
            if array[min_value]>array[j]:
                min_value=j

        array[i],array[min_value]=array[min_value],array[i]
    return array

""" 
array = [5,3,2,1,6,8,2,5,9]
print(selectionSort(array)) 
"""