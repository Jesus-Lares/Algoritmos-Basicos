import time
begin = time.time()

array = list(range(100000000))

def linearSearch(array,element,unique=True):
    indexList=[]
    for index,value in enumerate(array):
        if value == element:
            if unique:
                return index
            indexList.append(index)
    return indexList if not unique else -1


print(linearSearch(array,99988800))
finish = time.time()
print(finish-begin)