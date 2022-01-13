array=[45,15,35,2,18,68,48,69,48,32,12,10]

def sort(array,order="asc"):
    orderFunction = desc if order =="desc" else asc

    for index in range(1, len(array)):
        value=array[index]
        position=index

        while position>0 and orderFunction(value,array[position-1]):
            array[position-1] , array[position] = value,array[position-1]
            position-=1 

    return array

def asc(value,value2):
    return value<value2

def desc(value,value2):
    return value>value2

print(sort(array,"desc"))