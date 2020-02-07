import pathlib

def loadInputs(fileLocation):
    file = pathlib.Path(fileLocation)
    if file.exists():
        return file.read_text().split()
    else:
        print("Day 1 input file does not exist")

def getFuelFromMass(mass):
    return int((mass / 3) - 2)

def solvePuzzle1(fileLocation):
    inputs = loadInputs(fileLocation)
    totalFuel = 0
    for i in inputs:
        totalFuel += getFuelFromMass(int(i))

    print("Day 1 Puzle 1 Solution - " + str(totalFuel))

def solvePuzzle2(fileLocation):
    inputs = loadInputs(fileLocation)
    totalFuel = 0

    for i in inputs:
        nextFuel = int(i);

        while(True):
            fuel = getFuelFromMass(nextFuel)

            if fuel < 1:
                break

            nextFuel = fuel
            totalFuel += fuel

    print("Day 1 Puzle 2 Solution - " + str(totalFuel))