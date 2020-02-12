class Line:
    def __init__(self, x1, y1, x2, y2):
        self.X1 = x1
        self.Y1 = y1
        self.X2 = x2
        self.Y2 = y2

        self.MaxX = max(x1,x2)
        self.MinX = min(x1,x2)
        self.MaxY = max(y1,y2)
        self.MinY = min(y1,y2)

        self.A = y2 - y1
        self.B = x2 - x1
        self.C = self.A * x1 + self.B * y1

        self.Length = self.MaxX - self.MinX + self.MaxY - self.MinY

    def hasPoint(self, xIn, yIn):
        if xIn < self.MinX or xIn > self.MaxX or yIn < self.MinY or yIn > self.MaxY:
            return False
        else:
            return True

class Intersection:
    def __init__(self, xIn, yIn, wireLengthIn):
        self.X = xIn
        self.Y = yIn
        self.ManDist = abs(xIn) + abs(yIn)
        self.wireLength = wireLengthIn

def lengthBetweenTwoPoints(x1,y1,x2,y2):
    MaxX = max(x1,x2)
    MinX = min(x1,x2)
    MaxY = max(y1,y2)
    MinY = min(y1,y2)

    return MaxX - MinX + MaxY - MinY

def getWireLengthToPoint(index1, index2, p1, p2, line1, line2):
    length = 0

    for i in range(index1):
        length += line1[i].Length
    for i in range(index2):
        length += line2[i].Length

    length += lengthBetweenTwoPoints(line1[index1].X1, line1[index1].Y1, p1, p2)
    length += lengthBetweenTwoPoints(line2[index2].X1, line2[index2].Y1, p1, p2)

    return length

def convertStringToCoords(stringIn):
    coords = []

    instructions = stringIn.split(",")
    currentX = 0
    currentY = 0

    for i in instructions:
        dir = i[0:1]
        dist = int(i[1:])

        if dir == "R":
            coords.append(Line(currentX, currentY, currentX + dist, currentY))
            currentX += dist
        elif dir == "L":
            coords.append(Line(currentX, currentY, currentX - dist, currentY))
            currentX -= dist
        elif dir == "U":
            coords.append(Line(currentX, currentY, currentX, currentY + dist))
            currentY += dist
        elif dir == "D":
            coords.append(Line(currentX, currentY, currentX, currentY - dist))
            currentY -= dist
    
    return coords

def createIntersections(line1, line2):
    intersections = []

    for i in range(len(line1)):
        l = line1[i]

        for j in range(len(line2)):
            l2 = line2[j]

            denom = l.A * l2.B - l2.A * l.B

            if denom == 0:
                continue

            p1 = (l2.B * l.C - l.B * l2.C) / denom
            p2 = (l.A * l2.C - l2.A * l.C) / denom

            if l.hasPoint(p1,p2) and l2.hasPoint(p1,p2):
                l1pLength = lengthBetweenTwoPoints(l.X1, l.Y1, p1, p2)
                l2pLength = lengthBetweenTwoPoints(l2.X1, l2.Y1, p1, p2)

                totalWireLength = getWireLengthToPoint(i, j, p1, p2, line1, line2)

                intersections.append(Intersection(p1, p2, totalWireLength))

    return intersections