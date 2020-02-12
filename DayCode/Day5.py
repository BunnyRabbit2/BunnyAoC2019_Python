import pathlib
from AOCLibrary import IntcodeComputer

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split(",")
    else:
        print("Day 5 input file does not exist")

def solvePuzzle1(fileLocation):
    icp = IntcodeComputer.IntcodeComputer(loadInputs(fileLocation))

    icp.addInput(1)

    result = [0,False]

    while result[1] != True:
        result = icp.runProgram()

    print("Day 5 Puzzle 1 solution - " + str(result[0]))

def solvePuzzle2(fileLocation):
    icp = IntcodeComputer.IntcodeComputer(loadInputs(fileLocation))

    icp.addInput(5)

    result = [0,False]

    while result[1] != True:
        result = icp.runProgram()
    
    print("Day 5 Puzzle 2 solution - " + str(result[0]))