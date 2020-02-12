def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split(",")
    else:
        print("Day 1 input file does not exist")

def solvePuzzle1(fileLocation):
    icp = IntcodeComputer(loadInputs(fileLocation))

    icp.setValueToAddress(1, 12)
    icp.setValueToAddress(2, 2)

    result = icp.runProgram(0)

    print("Day2: Puzzle 1 solution - " + str(result))