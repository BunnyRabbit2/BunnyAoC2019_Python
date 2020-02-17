import pathlib
from AOCLibrary import AsteroidField

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        with file.open() as f:
            return f.read().splitlines()

def solvePuzzle1(fileLocation):
    afield = AsteroidField.AstField()
    afield.createField(loadInputs(fileLocation))
    best = afield.getBestPlacement()

    print("Day 10 Puzzle 1 solution - " + str(best.asteroidsInSight))

def solvePuzzle2(fileLocation):
    result = 0

    print("Day 10 Puzzle 2 solution - " + str(result))