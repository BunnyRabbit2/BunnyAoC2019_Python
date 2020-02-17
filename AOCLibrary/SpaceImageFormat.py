class SpaceImageFormat:
    def __init__(self, data, wIn, hIn):
        self.width = wIn
        self.height = hIn
        self.imageData = data
        self.layers = []
        self.colourData = []
        self.turnDataIntoLayers()
        self.createColourData()

    def turnDataIntoLayers(self):
        pixelsPerLayer = self.width * self.height
        noOfLayers = int(len(self.imageData) / pixelsPerLayer)

        for i in range(0,noOfLayers):
            newLayer = []
            startIndex = i + pixelsPerLayer

            for j in range(0,pixelsPerLayer):
                newLayer.append(self.imageData[startIndex + j])

            self.layers.append(newLayer)

    def createColourData(self):
        for p in self.layers[0]:
            self.colourData.append(p) # Copy first layer in

        for li, l in enumerate(self.layers):
            for pi, p in enumerate(self.colourData):
                if p == 2:
                    p = self.layers[li][pi]

    def verifyData(self):
        noOfZeroes = []

        for l in self.layers:
            zeroes = 0

            for p in l:
                if p == 0:
                    zeroes += 1

            noOfZeroes.append(zeroes)

        fewestZeroes = noOfZeroes.index(min(noOfZeroes))

        noOfOnes = 0
        noOfTwos = 0

        for p in self.layers[fewestZeroes]:
            if p == 1:
                noOfOnes += 1
            elif p == 2:
                noOfTwos += 1

        return noOfOnes * noOfTwos

    def drawImage(self):
        for h in range(0, len(self.colourData), self.width):
            line = ""
            for w in range(0,self.width):
                if self.colourData[h+w] == 0:
                    line += " "
                elif self.colourData[h+w] == 1:
                    line += "#"
            print(line)