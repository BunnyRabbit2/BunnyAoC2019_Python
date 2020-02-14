class OrbitTreeNode:
    def __init__(self, codeIn = "", pCodeIn = ""):
        self.parentCode = pCodeIn
        self.planetCode = codeIn
        self.distanceToRoot = -1
        self.root = True
        self.childNodes = []

class OrbitTree:
    def __init__(self):
        self.orbits = {}

    def createTree(self, orbitCodes):
        for parent, child in map(lambda s:s.split(')'), orbitCodes):
            if parent not in self.orbits:
                self.orbits[parent] = OrbitTreeNode(parent, "")
            if child not in self.orbits:
                self.orbits[child] = OrbitTreeNode(child, parent)
            else:
                self.orbits[child].parentCode = parent

            self.orbits[child].root = False
            self.orbits[parent].childNodes.append(self.orbits[child])

        self.setDistancesFromRoot()

    def setDistancesFromRoot(self):
        root = 0

        for c in self.orbits:
            if self.orbits[c].root:
                root = self.orbits[c]
                break

        for c in root.childNodes:
            self.setChildrenDistance(c)

    def setChildrenDistance(self, node):
        node.distanceToRoot = self.orbits[node.parentCode].distanceToRoot + 1
        for c in node.childNodes:
            self.setChildrenDistance(c)

    def getTotalOrbits(self):
        totalOrbits = 0

        for n in self.orbits:
            totalOrbits += self.orbits[n].distanceToRoot

        return totalOrbits

    def getDistanceBetweenTwoOrbits(self, startNode, endNode):
        distance = 0

        start = 0
        end = 0

        for o in self.orbits:
            if o == startNode:
                start = o
                break

        for o in self.orbits:
            if o == endNode:
                end = o
                break

        startRoute = self.getRouteToRoot(self.orbits[start])
        endRoute = self.getRouteToRoot(self.orbits[end])

        matchingNode = 0
        breakLoop = False

        for sNode in startRoute:
            for eNode in endRoute:
                if sNode.planetCode == eNode.planetCode:
                    matchingNode = eNode
                    breakLoop = True
                    break
            if breakLoop:
                break

        if matchingNode.parentCode != 0:
            distance = len(startRoute) + len(endRoute) - matchingNode.distanceToRoot * 2
            distance -= 4 # remove start, end and the crossover

        return distance

    def getRouteToRoot(self, nodeIn):
        route = []

        currentNode = nodeIn

        while not currentNode.root:
            route.append(currentNode)
            currentNode = self.orbits[currentNode.parentCode]

        return route