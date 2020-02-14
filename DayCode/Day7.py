import pathlib
import itertools
from AOCLibrary import IntcodeComputer

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split(",")
    else:
        print("Day 7 input file does not exist")

def solvePuzzle1(fileLocation):
    icp = IntcodeComputer.IntcodeComputer(loadInputs(fileLocation))

    phaseSettings = itertools.permutations([0,1,2,3,4])

    maxSignal = 0

    for ps in phaseSettings:
        signal = 0

        for s in ps:
            icp.addInput(s)
            icp.addInput(signal)

            result = [0,False]

            while result[1] != True:
                result = icp.runProgram()

            signal = result[0]

            icp.resetProgram()

        if signal > maxSignal:
            maxSignal = signal

    print("Day 7 Puzzle 1 solution - " + str(maxSignal))

def solvePuzzle2(fileLocation):
    program = loadInputs(fileLocation)

    amps = []
    for i in range(0,5):
        amps.append(IntcodeComputer.IntcodeComputer(program))

    phaseSettings = itertools.permutations([5,6,7,8,9])

    maxSignal = 0

    for ps in phaseSettings:
        signal = 0

        # first loop through the amps
        for i in range(0,5):
            amps[i].addInput(ps[i])
            amps[i].addInput(signal)

            signal = amps[i].runProgram()[0]

        results = []
        for i in range(0,5):
            results.append((0,False))
        
        while not results[4][1]:
            for i in range(0,5):
                amps[i].addInput(signal)
                results[i] = amps[i].runProgram()
                signal = results[i][0]

        if signal > maxSignal:
            maxSignal = signal

    print("Day 7 Puzzle 2 solution - " + str(maxSignal))