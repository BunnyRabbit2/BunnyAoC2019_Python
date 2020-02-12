import pathlib
from AOCLibrary import Wires

def solvePuzzle1(fileLocation):
    lines = []

    file = pathlib.Path(fileLocation)
    if file.exists():
        with file.open() as f:
            lines = f.readlines()

    line1Coords = Wires.convertStringToCoords(lines[0])
    line2Coords = Wires.convertStringToCoords(lines[1])
    intersections = Wires.createIntersections(line1Coords, line2Coords)

    currentShortest = intersections[0]

    for i in intersections:
        if i.ManDist < currentShortest.ManDist:
            currentShortest = i

    print("Day 3 Puzzle 1 Solution - " + str(currentShortest.ManDist))

def solvePuzzle2(fileLocation):
    lines = []

    file = pathlib.Path(fileLocation)
    if file.exists():
        with file.open() as f:
            lines = f.readlines()

    line1Coords = Wires.convertStringToCoords(lines[0])
    line2Coords = Wires.convertStringToCoords(lines[1])
    intersections = Wires.createIntersections(line1Coords, line2Coords)

    currentShortest = intersections[0]

    for i in intersections:
        if i.WireLength < currentShortest.WireLength:
            currentShortest = i

    print("Day 3 Puzzle 2 Solution - " + str(currentShortest.WireLength))