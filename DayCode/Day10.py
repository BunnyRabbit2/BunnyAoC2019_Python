import pathlib
from AOCLibrary import AsteroidField

AField = AsteroidField.AstField()

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        with file.open() as f:
            return f.read().splitlines()

def solvePuzzle1():
    print("Day 10 Puzzle 1 solution - " + str(AField.station.asteroidsInSight))

def solvePuzzle2():
    result = AField.getAsteroidDestroyedAtN(200)

    print("Day 10 Puzzle 2 solution - " + str(result.X * 100 + result.Y))