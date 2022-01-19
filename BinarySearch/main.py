import time
begin = time.time()

"""
def binarySearch(array,value,index=0):
    middle = len(array) // 2

    if middle == 0:
        return index+middle if value == array[middle] else -1

    if  value == array[middle]:
        return index+middle
    elif  value < array[middle]:
        return binarySearch(array[:middle],value,index)
    else:
        return binarySearch(array[middle:],value,index+middle)
""" 

def binarySearch(arr, l, r, x): 
    if r >= l: 
        mid = l + (r - l) // 2
 
        if arr[mid] == x:
            return mid 
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r , x)

    else:
        return -1

 
arr = list(range(1,100000000))
x = 10
 
#result = binarySearch(arr, x)                  ## First function
result = binarySearch(arr, 0, len(arr)-1, x)    ## Second function

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array") 

finish = time.time()
print(finish-begin) 