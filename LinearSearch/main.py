array = [1,2,3,8,5,6,7,8]

def linearSearch(array,element,unique=True):
    indexList=[]
    for index,value in enumerate(array):
        if value == element:
            if unique:
                return index
            indexList.append(index)
    return indexList if not unique else -1

print(linearSearch(array,0))