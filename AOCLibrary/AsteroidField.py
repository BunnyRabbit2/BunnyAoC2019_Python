import math
from operator import attrgetter

class Asteroid:
    AsteroidId = 0

    def __init__(self, xIn = -1, yIn = -1):
        self.X = xIn
        self.Y = yIn
        self.asteroidsInSight = 0
        self.id = Asteroid.AsteroidId
        self.distFromStation = 0
        Asteroid.AsteroidId += 1

class AstField:
    def __init__(self):
        self.astInPlace = []
        self.asteroids = []
        self.station = 0

    def createField(self, dataIn): # must be a 2D array
        height = len(dataIn)
        width = len(dataIn[0])

        for w in range(0,width):
            newArr = []
            for h in range(0,height):
                newArr.append(-1)
            self.astInPlace.append(newArr)

        for w in range(0,width):
            for h in range(0,height):
                if dataIn[h][w] == '#':
                    newA = Asteroid(w,h)
                    self.asteroids.append(newA)
                    self.astInPlace[w][h] = newA.id
    
    def setStation(self):
        bestPlacement = Asteroid()

        for a in self.asteroids:
            count = 0
            angles = []

            for b in self.asteroids:
                if a.id != b.id:
                    angle = getBearingBetweenAsteroids(a,b)

                    if angle not in angles:
                        angles.append(angle)
                        count += 1

            a.asteroidsInSight = count
        
        for a in self.asteroids:
            if a.asteroidsInSight > bestPlacement.asteroidsInSight:
                bestPlacement = a

        self.station = bestPlacement

    def getAsteroidDestroyedAtN(self, n):
        targets = {}

        for a in self.asteroids:
            angle = getBearingBetweenAsteroids(self.station, a)
            if angle not in targets:
                targets[angle] = []
            targets[angle].append(a)
            a.distFromStation = distanceBetweenAsteroids(self.station,a)

        keysInOrder = sorted(targets.keys())

        for l in targets.values():
            l.sort(key=attrgetter('distFromStation'))

        nthAst = 0
        keyIdx = 0
        for i in range(0,n):
            circuit = []
            while True:
                circuit = targets[keysInOrder[keyIdx]]
                keyIdx = (keyIdx + 1) % len(keysInOrder)
                if len(circuit) != 0:
                    break

            nthAst = circuit[0]
            circuit.pop()

        return nthAst

                
def distanceBetweenAsteroids(ast1, ast2):
    return math.sqrt((ast1.X - ast2.X)**2 + (ast1.Y - ast2.Y)**2)

def getBearingBetweenAsteroids(ast1, ast2, returnDegrees = True):
    a = ast1.X - ast2.X
    o = ast1.Y - ast2.Y

    theta = math.atan2(o,a)

    if returnDegrees:
        return theta * (180/3.142)
    else:
        return theta
