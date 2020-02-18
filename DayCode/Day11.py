import pathlib
from AOCLibrary.HullPainting import HullPainterRobot

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split(",")
    else:
        print("Day 11 input file does not exist")

def solvePuzzle1(fileLocation):
    robot = HullPainterRobot(loadInputs(fileLocation))
    robot.paintPanels(0)

    result = robot.panelsPainted()

    print("Day 11 Puzzle 1 solution - " + str(result))

def solvePuzzle2(fileLocation):
    result = 0

    print("Day 11 Puzzle 2 solution - " + str(result))