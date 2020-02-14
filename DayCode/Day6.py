import pathlib
import re
from AOCLibrary import Orbits

def loadInputs(fileLocation):
    lines = []

    file = pathlib.Path(fileLocation)
    if file.exists():
        with file.open() as f:
            lines = f.read().splitlines()
            return lines
    else:
        print("Day 6 input file does not exist")

def solvePuzzle1(fileLocation):
    result = 0

    oTree = Orbits.OrbitTree()
    oTree.createTree(loadInputs(fileLocation))

    result = oTree.getTotalOrbits()

    print("Day 6 Puzzle 1 solution - " + str(result))

def solvePuzzle2(fileLocation):
    result = 0

    oTree = Orbits.OrbitTree()
    oTree.createTree(loadInputs(fileLocation))

    result = oTree.getDistanceBetweenTwoOrbits("YOU","SAN")
    
    print("Day 6 Puzzle 2 solution - " + str(result))