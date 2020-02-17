import math

class Asteroid:
    AsteroidId = 0

    def __init__(self, xIn = -1, yIn = -1):
        self.X = xIn
        self.Y = yIn
        self.asteroidsInSight = 0
        self.id = Asteroid.AsteroidId
        Asteroid.AsteroidId += 1

class AstField:
    def __init__(self):
        self.astInPlace = []
        self.asteroids = []

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
    
    def getBestPlacement(self):
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

        return bestPlacement
                
def distanceBetweenAsteroids(ast1, ast2):
    return math.sqrt((ast1.X - ast2.X)**2 + (ast1.Y - ast2.Y)**2)

def getBearingBetweenAsteroids(ast1, ast2, returnDegrees = True):
    x1 = ast1.X
    y1 = ast1.Y
    x2 = ast2.X
    y2 = ast2.Y
    a = 0
    o = 0

    if y1 < y2:
        a = y2 - y1
    else:
        a = y1 - y2

    if x1 < x2:
        o = x2 - x1
    else:
        o = x1 - x2

    theta = math.atan2(o,a)

    theta = theta * (180/3.142)

    if y1 < y2: # South of point
        if x1 > x2:
            theta = 180 + theta # east of point
        else:
            theta = 180 - theta # west of point
    else:
        if x1 > x2:
            theta = 360 - theta # north of point

    if returnDegrees:
        return theta
    else:
        return theta * (3.142/180)
