class IntcodeComputer:
    def __init__(self, program):
        self.result = 0
        self.relativeBase = 0
        self.program = program
        self.initialProgram = program
        self.extraMemory = []
        self.readAddress = 0
        self.inputs = []

    def resetProgram(self):
        self.result = 0
        self.relativeBase = 0
        self.program = list(self.initialProgram)
        self.extraMemory = []
        self.readAddress = 0
        self.inputs = []

    def addInput(self, input):
        self.inputs.append(input)

    def setValueToAddress(self, address, value):
        if address >= len(self.program):
            newAdd = address - len(self.program)
            self.extraMemory[str(newAdd)] = value
        else:
            self.program[address] = value

    def getValueFromAddress(self, address):
        if (address >= len(self.program)):
            return self.extraMemory[str(address)]
        else:
            return self.program[address]

    def setValue(self, param, mode):
        if mode == 1:
            return param
        elif mode == 2:
            return self.getValueFromAddress(param + self.relativeBase)
        else: return self.getValueFromAddress(param)

    def runProgram(self, resultAddress = -1):
        currentInput = 0
        output = 0
        terminated = False
        self.program = [int(p) for p in self.program]

        while True:
            if self.program[self.readAddress] == 99:
                break

            opcode = self.program[self.readAddress] % 10

            firstMode = int((self.program[self.readAddress] / 100) % 10)
            secondMode = int((self.program[self.readAddress] / 1000) % 10)
            thirdMode = int((self.program[self.readAddress] / 10000) % 10)

            firstParam = 0
            secondParam = 0
            thirdParam = 0

            if self.readAddress + 1 < len(self.program) - 1:
                firstParam = self.program[self.readAddress+1]
            if self.readAddress + 2 < len(self.program) - 1:
                secondParam = self.program[self.readAddress+2]
            if self.readAddress + 3 < len(self.program) - 1:
                thirdParam = self.program[self.readAddress+3]

            if opcode == 3:
                if currentInput < len(self.inputs):
                    if firstMode == 2:
                        self.setValueToAddress(firstParam + self.relativeBase, self.inputs[currentInput])
                    else:
                        self.setValueToAddress(firstParam, self.inputs[currentInput])
                    currentInput += 1
                    self.readAddress += 2
                else:
                    print("IntcodeComputer Error. Asked for input not provided")
                continue
            elif opcode == 4:
                if firstMode == 1:
                    output = firstParam
                elif firstMode == 2:
                    output = self.getValueFromAddress(firstParam + self.relativeBase)
                else:
                    output = self.getValueFromAddress(firstParam)

                self.readAddress += 2
                if secondParam == 99:
                    terminated = True
                else:
                    terminated = False

                return (output, terminated)

            firstValue = self.setValue(firstParam, firstMode)
            secondValue = self.setValue(secondParam, secondMode)
            thirdValue = thirdParam + relativeBase if thirdMode == 2 else thirdParam

            if opcode == 1:
                self.setValueToAddress(thirdValue, firstValue + secondValue)
                self.readAddress += 4
                continue
            elif opcode == 2:
                self.setValueToAddress(thirdValue, firstValue * secondValue)
                self.readAddress += 4
                continue
            elif opcode == 5:
                if firstValue != 0:
                    self.readAddress = secondValue
                else:
                    self.readAddress += 3
                continue
            elif opcode == 6:
                if firstValue == 0:
                    self.readAddress = secondValue
                else:
                    self.readAddress += 3
                continue
            elif opcode == 7:
                if firstValue < secondValue:
                    self.setValueToAddress(thirdValue, 1)
                else:
                    self.setValueToAddress(thirdValue, 0)
                self.readAddress += 4
                continue
            elif opcode == 8:
                if (firstValue == secondValue):
                    self.setValueToAddress(thirdValue, 1)
                else:
                    self.setValueToAddress(thirdValue, 0)
                self.readAddress += 4
                continue
            elif opcode == 9:
                self.relativeBase += firstValue
                self.readAddress += 2
                continue
            else:
                print("IncodeComputer Error. Program opcode not recognised")

        terminated = True
        if resultAddress == -1:
            return output
        else:
            return self.getValueFromAddress(resultAddress)