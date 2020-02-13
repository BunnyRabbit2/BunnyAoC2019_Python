import pathlib

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split(",")
    else:
        print("Day 6 input file does not exist")

def solvePuzzle1(fileLocation):
    result = 0

    print("Day 5 Puzzle 1 solution - " + str(result))

def solvePuzzle2(fileLocation):
    result = 0
    
    print("Day 6 Puzzle 2 solution - " + str(result))