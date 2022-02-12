def orderArray(arrayLeft,arrayRight):
    newArray=[]
    i,j=0,0
    while len(arrayLeft) != i or len(arrayRight) != j:
        left = arrayLeft[i] if len(arrayLeft) != i else arrayRight[j]*10 
        right = arrayRight[j] if len(arrayRight) != j else arrayLeft[i]*10 

        if left < right:
            i+=1
            newArray.append(left)
        else:
            j+=1
            newArray.append(right)

    return newArray

def mergeSort(array):
    if len(array)<=1:
        return array
    
    middle = len(array)//2

    left=mergeSort(array[:middle])
    right=mergeSort(array[middle:])
    
    return orderArray(left,right)

""" 
array=[97,41,99,44,45,18,68,48,69,48,32,12,10]
print(mergeSort(array)) 
"""