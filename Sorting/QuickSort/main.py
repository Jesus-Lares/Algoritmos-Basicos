
def quickSort(arr):
    if len(arr) <= 1:
        return arr

    left  = []
    right = []
    equal = []
    pivot = arr[-1]
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)

    return quickSort(left) + equal + quickSort(right)

""" 
array=[97,41,99,44,45,18,68,48,69,48,32,12,10]
print(quickSort(array)) 
"""