def orderArray(arrayLeft,arrayRight):
    newArray=[]
    while len(arrayLeft) != 0 or len(arrayRight) != 0:
        left = arrayLeft[0] if len(arrayLeft) != 0 else arrayRight[0]*10 
        right = arrayRight[0] if len(arrayRight) != 0 else arrayLeft[0]*10 

        if left < right:
            arrayLeft.pop(0)
            newArray.append(left)
        else:
            arrayRight.pop(0)
            newArray.append(right)

    return newArray

def mergeSort(array):
    if len(array)<=1:
        return array
    
    middle = len(array)//2

    left=mergeSort(array[:middle])
    right=mergeSort(array[middle:])
    
    return orderArray(left,right)


array=[97,41,99,44,45,18,68,48,69,48,32,12,10]
print(mergeSort(array))