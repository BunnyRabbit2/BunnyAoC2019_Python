import pathlib

def checkPasswordPuzzle1(pIn):
    pIn = str(pIn)

    if(len(pIn) != 6):
        return False

    hasDouble = False

    for i in range(0,5):
        if pIn[i] > pIn[i+1]:
            return False

        if pIn[i] == pIn[i+1]:
            hasDouble = True
        
    return hasDouble

def getPuzzle1CorrectPasswordNumber(checkMin, checkMax):
    correctPasswords = []

    for i in range(int(checkMin),int(checkMax)):
        if(checkPasswordPuzzle1(i)):
            correctPasswords.append(i)
    
    return len(correctPasswords)

def checkPasswordPuzzle2(pIn):
    pIn = str(pIn)

    if(len(pIn) != 6):
        return False

    hasDouble = False

    for i in range(0,5):
        if pIn[i] > pIn[i+1]:
            return False

        if pIn[i] == pIn[i+1]:
            if i == 4:
                if pIn[i-1] != pIn[i]:
                    hasDouble = True
            elif i == 0:
                if pIn[i+1] != pIn[i+2]:
                    hasDouble = True
            elif pIn[i-1] != pIn[i] and pIn[i+1] != pIn[i+2]:
                hasDouble = True
        
    return hasDouble

def getPuzzle2CorrectPasswordNumber(checkMin, checkMax):
    correctPasswords = []

    for i in range(int(checkMin),int(checkMax)):
        if(checkPasswordPuzzle2(i)):
            correctPasswords.append(i)
    
    return len(correctPasswords)