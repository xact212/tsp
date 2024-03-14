def TSPBS(inpGraph):
    bestPath = [] #define constants
    numNodes = len(inpGraph)
    bestCost = float("inf")
    def _TSP(currPath, currCost):
        nonlocal bestCost #nessecary to tell closure to treat these varaibles within the parent's scope
        nonlocal bestPath
        #checks to end recursion
        if len(currPath) == numNodes: #terminate if path length is the same as the number of nodes in the graph
            currCost += inpGraph[currPath[len(currPath) - 1]][0] #add the connection to the first node
            if currCost < bestCost: #only replace the best path if the current path has a smaller weighted sum
                bestCost = currCost
                bestPath = currPath.copy()
            return
        if currCost >= bestCost: #terminate early if the current cost is already worse than the best cost 
            return
        adjacent = inpGraph[currPath[len(currPath) - 1]] #get all the edges from the current node
        for edge in range(len(adjacent)): #try adding all of them to the stack
            if edge in currPath:
                continue
            if adjacent[edge] == 0:
                continue
            currPath.append(edge)
            _TSP(currPath, currCost + adjacent[edge])
            currPath.pop()
    _TSP([0], 0)
    bestPath.append(0) #add the last (first) node at the end so we don't have to do it every time we find a new best path
    return (bestCost, bestPath)           

G = [
[0, 2, 3, 20, 1],
[2, 0 , 15, 2, 20],
[3, 15, 0, 20, 13],
[20, 2, 20, 0, 9],
[1, 20, 13, 9, 0]
]

print(TSPBS(G))
