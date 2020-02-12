import pathlib
from AOCLibrary import PasswordChecker

def solvePuzzle1(fileLocation):
    checkMin = -1
    checkMax = -1
    numbers = []

    file = pathlib.Path(fileLocation)
    if file.exists():
        numbers = file.read_text().split("-")
        checkMin = numbers[0]
        checkMax = numbers[1]

    solution = PasswordChecker.getPuzzle1CorrectPasswordNumber(checkMin,checkMax)

    print("Day 4 Puzzle 1 - " + str(solution))

def solvePuzzle2(fileLocation):
    checkMin = -1
    checkMax = -1
    numbers = []

    file = pathlib.Path(fileLocation)
    if file.exists():
        numbers = file.read_text().split("-")
        checkMin = numbers[0]
        checkMax = numbers[1]

    solution = PasswordChecker.getPuzzle2CorrectPasswordNumber(checkMin,checkMax)

    print("Day 4 Puzzle 2 - " + str(solution))