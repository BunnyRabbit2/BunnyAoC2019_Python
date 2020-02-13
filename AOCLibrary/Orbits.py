class OrbitTreeNode:
    def __init__(self):
        self.parentNode = 0
        self.parentCode = ""
        self.planetCode = ""
        self.distanceToRoot = -1
        self.childNodes = []

    def __init__(self, codeIn, pCodeIn):
        self.parentNode = 0
        self.parentCode = pCodeIn
        self.planetCode = codeIn
        self.distanceToRoot = -1
        self.childNodes = []

class OrbitTree:
    def __init__(self):
        self.orbits = []

    def createTree(self, orbitCodes):
        for o in orbitCodes:
            addOrbitToTree(o)

        setParentChildRelationships()

        setDistancesFromRoot()

    def addOrbitToTree(self, orbitCode):
        codes = orbitCode.split(")")

        node = OrbitTreeNode()

        pIndex = -1
        cIndex = -1

        for i in range(0,len(self.orbits)):
            if self.orbits[i].planetCode == codes[0]:
                pIndex = i
            if self.orbits[i].planetCode == codes[1]:
                cIndex = i

        if pIndex == -1:
            self.orbits.append(OrbitTreeNode(parent,""))

        if cIndex != -1:
            self.orbits[cIndex].parentCode = codes[0]
        else:
            self.orbits.append(OrbitTreeNode(codes[1],coes[0]))

    def setParentChildRelationships(self):
        for otn in self.orbits:
            pIndex = -1

            for i in range(0,len(self.orbits)):
                if self.orbits[i].planetCode == otn.parentCode:
                    pIndex = i
                    break

            if pIndex != -1:
                otn.parentNode = self.orbits[pIndex]
                self.orbits[pIndex].childNodes.append(otn)

    def setDistancesFromRoot(self)
        rIndex = -1 # root index

        for i in range(0,len(self.orbits)):
            if self.orbits[i].planetCode == "":
                rIndex = i
                break

        root = self.orbits[rIndex]
        root.distanceToRoot = 0

        for c in root.childNodes:
            setChildrenDistance(c)

    def setChildrenDistance(self, node):
        node.distanceToRoot = node.parentNode.distanceToRoot + 1
        for c in root.childNodes:
            setChildrenDistance(c)

    def getTotalOrbits(self):
        totalOrbits = 0

        for n in self.orbits:
            totalOrbits += n.distanceToRoot

        return totalOrbits

    def getDistanceBetweenTwoOrbits(self, startNode, endNode):
        distance = 0

        start = 0
        end = 0

        for i in range(0,len(self.orbits)):
            if self.orbits[i].planetCode == startNode:
                start = self.orbits[i]
                break

        for i in range(0,len(self.orbits)):
            if self.orbits[i].planetCode == endNode:
                end = self.orbits[i]
                break

        startRoute = getRouteToRoot(start)
        endRoute = getRouteToRoot(end)

        matchingNode = 0
        breakLoop = False

        for sNode in startRoute:
            for eNode in endRoute:
                if sNode.planetCode == eNode.planetCode
                    matchingNode = eNode
                    breakLoop = True
                    break
            if breakLoop:
                break

        if matchingNode.parentCode != 0:
            distance = len(startRoute) + len(endRoute) - matchingNode.distanceToRoot * 2
            distance -= 2

        return distance

        def getRouteToRoot(self, nodeIn):
            route = []

            currentNode = nodeIn

            while currentNode.parentCode != "":
                route.append(currentNode)
                currentNode = currentNode.parentNode

            return route