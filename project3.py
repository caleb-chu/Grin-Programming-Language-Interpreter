# project3.py
#
# ICS 33 Fall 2023
# Project 3: Why Not Smile?
#
# The main module that executes your Grin interpreter.
#
# WHAT YOU NEED TO DO: You'll need to implement the outermost shell of your
# program here, but consider how you can keep this part as simple as possible,
# offloading as much of the complexity as you can into additional modules in
# the 'grin' package, isolated in a way that allows you to unit test them.

import grin
from grin import GrinTokenKind


def appendObjects(objList, tokenLine, varDict, labelDict, tokenList, tokenLineCounter):
    """Append objects based on token line information to the object list.

    Args:
    - objList: List to store objects representing operations.
    - tokenLine: List representing the current line of tokens.
    - varDict: Dictionary containing variables and their values.
    - labelDict: Dictionary containing labels and their positions.
    - tokenList: List of tokenized lines.
    - tokenLineCounter: Counter representing the current line number.
    """
    if tokenLine[0].text() == 'END':  # Doesn't work properly
        objList.append("END")
    elif tokenLine[0].text() == 'LET':
        letObj = grin.Let(varDict, tokenLine[1].text(), tokenLine[2].value(), tokenLine[2].kind())
        objList.append(letObj)
    elif tokenLine[0].text() == 'PRINT':
        printObj = grin.Print(varDict, tokenLine[1].text(), tokenLine[1].kind())
        objList.append(printObj)
    elif tokenLine[0].text() == 'INNUM':
        tempValue = input()
        innumObj = grin.INNUM(tokenLine[1].text(), tempValue, varDict)
        objList.append(innumObj)
    elif tokenLine[0].text() == 'INSTR':
        tempValue = input()
        instrObj = grin.INSTR(tokenLine[1].text(), tempValue, varDict)
        objList.append(instrObj)
    elif tokenLine[0].text() == 'ADD':
        addObj = grin.ADD(varDict, tokenLine[1].text(), tokenLine[2].value(), tokenLine[1].kind(),
                          tokenLine[2].kind())
        objList.append(addObj)
    elif tokenLine[0].text() == 'SUB':
        subObj = grin.SUB(varDict, tokenLine[1].text(), tokenLine[2].value(), tokenLine[1].kind(),
                          tokenLine[2].kind())
        objList.append(subObj)
    elif tokenLine[0].text() == 'MULT':
        multObj = grin.MULT(varDict, tokenLine[1].text(), tokenLine[2].value(), tokenLine[1].kind(),
                            tokenLine[2].kind())
        objList.append(multObj)
    elif tokenLine[0].text() == 'DIV':
        divObj = grin.DIV(varDict, tokenLine[1].text(), tokenLine[2].value(), tokenLine[1].kind(),
                          tokenLine[2].kind())
        objList.append(divObj)
    elif tokenLine[0].text() == 'GOTO':
        if tokenLine[1].kind() is GrinTokenKind.LITERAL_INTEGER and len(tokenLine) <= 2:  # GOTO 3 or GOTO -3
            gotoObj = grin.GOTO(tokenLine[1].value(), len(tokenList))
            objList.append(gotoObj)
        elif len(tokenLine) <= 2:  # GOTO "CZ"
            gotoLabel = grin.GOTOLabel(labelDict, tokenLine[1].value())
            objList.append(gotoLabel)
        elif len(tokenLine) >= 5:
            detTrueObj = grin.conditional(tokenLine[1].value(), tokenLine[3].text(), tokenLine[4].text(), tokenLine[5].text(), varDict, len(tokenList), tokenLine[5].kind())
            objList.append(detTrueObj)
    elif tokenLine[0].text() == 'GOSUB':
        if tokenLine[1].kind() is GrinTokenKind.LITERAL_INTEGER and len(tokenLine) <= 2:  # GOTO 3 or GOTO -3
            gotoObj = grin.GOTO(tokenLine[1].value(), len(tokenList))
            objList.append(gotoObj)
        elif len(tokenLine) <= 2:  # GOTO "CZ"
            gotoLabel = grin.GOTOLabel(labelDict, tokenLine[1].value())
            objList.append(gotoLabel)
        elif len(tokenLine) >= 5:
            detTrueObj = grin.conditional(tokenLine[1].value(), tokenLine[3].text(), tokenLine[4].text(), tokenLine[5].text(), varDict, len(tokenList), tokenLine[5].kind())
            objList.append(detTrueObj)
    else:
        # is label
        labelDict[tokenLine[0].text()] = tokenLineCounter
        if tokenLine[2].text() == 'END':  # Doesn't work properly
            objList.append("END")
        elif tokenLine[2].text() == 'LET':
            letObj = grin.Let(varDict, tokenLine[3].text(), tokenLine[4].value(),
                              tokenLine[4].kind())
            objList.append(letObj)
        elif tokenLine[2].text() == 'PRINT':
            printObj = grin.Print(varDict, tokenLine[3].text(), tokenLine[3].kind())
            objList.append(printObj)
        elif tokenLine[2].text() == 'INNUM':
            tempValue = input()
            innumObj = grin.INNUM(tokenLine[3].text(), tempValue, varDict)
            objList.append(innumObj)
        elif tokenLine[2].text() == 'INSTR':
            tempValue = input()
            instrObj = grin.INSTR(tokenLine[3].text(), tempValue, varDict)
            objList.append(instrObj)
        elif tokenLine[2].text() == 'ADD':
            addObj = grin.ADD(varDict, tokenLine[3].text(), tokenLine[4].text(),
                              tokenLine[3].kind(),
                              tokenLine[4].kind())
            objList.append(addObj)
        elif tokenLine[2].text() == 'SUB':
            subObj = grin.SUB(varDict, tokenLine[3].text(), tokenLine[4].text(),
                              tokenLine[3].kind(),
                              tokenLine[4].kind())
            objList.append(subObj)
        elif tokenLine[2].text() == 'MULT':
            multObj = grin.MULT(varDict, tokenLine[3].text(), tokenLine[4].text(),
                                tokenLine[3].kind(),
                                tokenLine[4].kind())
            objList.append(multObj)
        elif tokenLine[2].text() == 'DIV':
            divObj = grin.DIV(varDict, tokenLine[3].text(), tokenLine[4].text(),
                              tokenLine[3].kind(),
                              tokenLine[4].kind())
            objList.append(divObj)
        elif tokenLine[2].text() == 'GOTO':
            if tokenLine[1].kind() is GrinTokenKind.LITERAL_INTEGER and len(tokenLine) <= 2:  # GOTO 3 or GOTO -3
                gotoObj = grin.GOTO(tokenLine[1].text(), len(tokenList))
                objList.append(gotoObj)
            elif len(tokenLine) <= 2:  # GOTO "CZ"
                gotoLabel = grin.GOTOLabel(labelDict, tokenLine[1].text())
        elif tokenLine[2].text() == 'GOSUB':
            pass
        else:
            pass
def runProgram(tokenList, varDict):
    """Execute the program based on the provided token list and variable dictionary.

    Args:
    - tokenList: List of tokenized lines.
    - varDict: Dictionary containing variables and their values.

    Returns:
    - None
    """
    labelDict = {}
    objList = []
    tokenLineCounter = 1
    for tokenLine in tokenList:
        appendObjects(objList, tokenLine, varDict, labelDict, tokenList, tokenLineCounter)
        tokenLineCounter += 1
    posTracker = 0

    while True:
        lineCurrentlyExecuting = posTracker + 1 #tracker var
        if objList[posTracker] == "END":
            break
        else:
            tempPos = objList[posTracker].execute(lineCurrentlyExecuting)
        if tempPos is None:
            posTracker += 1
        else:
            posTracker = tempPos

        if (posTracker + 1) > len(objList):
            break
def main() -> None:
    grinLines = []
    while True:
        tempInput = input()
        grinLines.append(tempInput)
        if tempInput == ".": #signifies end of program
            break

    #grinLines will be a list of user inputs

    #tries to parse tokens, will raise error if tokens cannot be parsed
    all_parsed_tokens = []
    parseWorked = False
    try:
        all_parsed_tokens = list(grin.parse(grinLines))
        parseWorked = True
    except grin.GrinParseError as e:
        print(f"Grin parse error: {e}")
    except Exception as e:
        print(f"Invalid Grin Statement: {e}")

    if parseWorked:
        varDict = {} #dictionary is outside for unit test purposes
        runProgram(all_parsed_tokens, varDict)


if __name__ == '__main__':
    main()
