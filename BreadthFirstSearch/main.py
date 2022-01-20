graph={
    'a':['b','c','g'],
    'b':['a','d','g'],
    'c':['a','d','e'],
    'd':['b','c','f'],
    'e':['c','f','g'],
    'f':['d','e','h'],
    'g':['a','b','e'],
    'h':['f'],
}

def returnNewNodes(searchList,graph):
    newVertex=[]
    interactions=[]
    for node in searchList:
        for childNode in graph[node]:
            if childNode not in searchList and childNode not in newVertex:
                interactions.append([node,childNode])
                newVertex.append(childNode)
    return newVertex,interactions

def anchura(initialPoint,graph):

    searchList=[initialPoint]
    interactions = []
    while len(searchList)!=len(list(graph.keys())):
        newVertex,newInteraction = returnNewNodes(searchList,graph)
        searchList += newVertex
        interactions += newInteraction 

    return interactions,searchList 

initialPoint=input("Digite el valor raiz: ")
interactions,searchList = anchura(initialPoint,graph)
print(f"Search in the order \n{searchList}\nand the intereactions to get there are \n{interactions}")