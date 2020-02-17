import pathlib
from AOCLibrary import SpaceImageFormat

def loadInputs(fileLocation):
    lines = []

    file = pathlib.Path(fileLocation)
    if file.exists():
        with file.open() as f:
            lines = f.readlines()

    numbers = []

    for c in lines[0]:
        numbers.append(int(c))

    return numbers

def solvePuzzle1(fileLocation):
    result = 0

    image = SpaceImageFormat.SpaceImageFormat(loadInputs(fileLocation),25,6)

    result = image.verifyData()

    print("Day 6 Puzzle 1 solution - " + str(result))

def solvePuzzle2(fileLocation):
    image = SpaceImageFormat.SpaceImageFormat(loadInputs(fileLocation),25,6)

    image.drawImage()