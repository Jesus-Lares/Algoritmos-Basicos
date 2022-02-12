
def profundidad(initialPoint,graph):
    keysList=list(graph.keys())
    interactions=[]
    searchList=[initialPoint]

    backwardValue=1

    while len(searchList)!=len(keysList) :
        backward=True
        for nextNode in keysList:
            if nextNode in graph[searchList[-backwardValue]]  and nextNode not in searchList:
                interactions.append((searchList[-backwardValue],nextNode))
                backward=False
                backwardValue=1
                searchList.append(nextNode)
                break
        if backward:
            backwardValue+=1
    return searchList,interactions

graph={
    'a':['b','c','g'],
    'b':['a','d'],
    'c':['a','d','e'],
    'd':['b','c','f'],
    'e':['c','f','g'],
    'f':['d','e','h'],
    'g':['a','e'],   
    'h':['f'],
}
initialPoint=input("initial point: ")

searchList,interactions = profundidad(initialPoint,graph)
print(f"the paht is \n{searchList} and the interactions to get there are \n{interactions}")