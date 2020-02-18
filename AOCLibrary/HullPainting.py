from enum import Enum
from AOCLibrary.IntcodeComputer import IntcodeComputer

class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Direction:
    DirectionValues = {
        Directions.UP: [0,-1],
        Directions.RIGHT: [1,0],
        Directions.DOWN: [0,1],
        Directions.LEFT: [-1,0]
    }

    def turnRight(directionIn):
        if directionIn.value >= len(Direction.DirectionValues) - 1:
            directionIn = Directions(0)
        else:
            directionIn = Directions(directionIn.value + 1)

        return directionIn

    def turnLeft(directionIn):
        if directionIn.value == 0:
            directionIn = Directions(len(Direction.DirectionValues) - 1)
        else:
            directionIn = Directions(directionIn.value - 1)

        return directionIn

class HullPainterRobot:
    def __init__(self, programIn):
        self.icp = IntcodeComputer(programIn)
        self.hullPaint = []
        self.panels = {}
        self.positionX = 0
        self.positionY = 0
        self.directionFacing = Directions.UP

    def paintPanels(self, startingPaintColour):
        output = [0,False]
        nextInput = startingPaintColour

        self.panels[(0,0)] = startingPaintColour

        while(not output[1]):
            if (self.positionX,self.positionY) not in self.panels:
                self.panels[(self.positionX,self.positionY)] = 0

            self.icp.addInput(self.panels[(self.positionX,self.positionY)])

            output = self.icp.runProgram()

            self.panels[(self.positionX,self.positionY)] = output[0]

            if output[1]:
                break

            output = self.icp.runProgram()

            if output[0] == 0:
                self.directionFacing = Direction.turnLeft(self.directionFacing)
            elif output[0] == 1:
                self.directionFacing = Direction.turnRight(self.directionFacing)

            xMove = Direction.DirectionValues[self.directionFacing][0]
            yMove = Direction.DirectionValues[self.directionFacing][1]

            self.positionX += xMove
            self.positionY += yMove

    def panelsPainted(self):
        return len(self.panels)

    def drawPoint(self, x, y, value):
        paint = ' '

        while len(self.hullPaint) - 1 < y:
            self.hullPaint.append([])

        while len(self.hullPaint[y]) - 1 < x:
            self.hullPaint[y].append(paint)

        if value == 1:
            paint = '#'

        self.hullPaint[y][x] = paint

    def transferPanelsToPaint(self):
        minX = 0
        minY = 0

        for pair in self.panels:
            pX = pair[0]
            pY = pair[1]

            if pX < minX :
                minX = pX
            if pY < minY:
                minY = pY

        if minX < 0:
            minX = abs(minX)
        else:
            minX = 0
        if minY < 0:
            minY = abs(minY)
        else:
            minY = 0

        for pair in self.panels:
            self.drawPoint(pair[0] + minX, pair[1] + minY, self.panels[pair])

    def displayHullPaint(self):
        self.transferPanelsToPaint()

        for line in self.hullPaint:
            s = ""
            print(s.join(line))
