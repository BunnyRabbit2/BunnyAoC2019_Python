import pathlib
from AOCLibrary import IntcodeComputer

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split(",")
    else:
        print("Day 2 input file does not exist")

def solvePuzzle1(fileLocation):
    icp = IntcodeComputer.IntcodeComputer(loadInputs(fileLocation))

    icp.setValueToAddress(1, 12)
    icp.setValueToAddress(2, 2)

    result = icp.runProgram(0)

    print("Day 2 Puzzle 1 solution - " + str(result))

def solvePuzzle2(fileLocation):
    icp = IntcodeComputer.IntcodeComputer(loadInputs(fileLocation))

    wantedResult = 19690720
    noun = 0
    verb = 0

    for n in range(99):
        for v in range(99):
            icp.resetProgram()

            icp.setValueToAddress(1, n)
            icp.setValueToAddress(2, v)

            test = icp.runProgram(0)

            if test == wantedResult:
                noun = n
                verb = v
                n = 99
                v = 99
            
    solution = 100 * noun + verb

    print("Day 2 Puzzle 2 solution - " + str(solution))