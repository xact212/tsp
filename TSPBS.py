def TSPBS(inpGraph):
    bestPath = []
    numNodes = len(inpGraph)
    bestCost = float("inf")
    def _TSP(currPath, currCost):
        nonlocal bestCost
        nonlocal bestPath
        if len(currPath) == numNodes:
            currCost += inpGraph[currPath[len(currPath) - 1]][0] #add the connection to the first node
            if currCost < bestCost:
                bestCost = currCost
                bestPath = currPath.copy()
            return
        if currCost >= bestCost:
            return
        adjacent = inpGraph[currPath[len(currPath) - 1]]
        for edge in range(len(adjacent)):
            if edge in currPath:
                continue
            if adjacent[edge] == 0:
                continue
            currPath.append(edge)
            _TSP(currPath, currCost + adjacent[edge])
            currPath.pop()
    _TSP([0], 0)
    bestPath.append(0)
    return (bestCost, bestPath)           

G = [
[0, 2, 3, 20, 1],
[2, 0 , 15, 2, 20],
[3, 15, 0, 20, 13],
[20, 2, 20, 0, 9],
[1, 20, 13, 9, 0]
]

print(TSPBS(G))
