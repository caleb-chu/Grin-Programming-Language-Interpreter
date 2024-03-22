from grin import GrinTokenKind


class GOTO:
    def __init__(self, jumpNumber, totalLines):
        self.jumpNumber = jumpNumber
        self.totalLines = totalLines

    def execute(self, lineNumber):
        if lineNumber + int(self.jumpNumber) > self.totalLines or lineNumber + int(self.jumpNumber) < 1:
            print("Out of range")
        else:
            return int(lineNumber + self.jumpNumber-1)

class GOTOLabel:
    def __init__(self, labelDict, labelName):
        self.labelDict = labelDict
        self.labelName = labelName

    def execute(self, lineNumber):
        if self.labelName in self.labelDict:
            return self.labelDict[self.labelName]
        else:
            print("label does not exist")



class conditional:
    def __init__(self, jumpNumber, compare1, operator, compare2, varDict, totalLines, compare2kind):
        self.val1 = 0
        self.val2 = 0
        self.jumpNumber = jumpNumber
        self.compare1 = compare1
        self.operator = operator
        self.compare2 = compare2
        self.varDict = varDict
        self.totalLines = totalLines
        self.compare2kind = compare2kind

    def execute(self, lineNumber):
        if self.determineTrue(self.compare1, self.operator,self.compare2, self.varDict, self.compare2kind):
            if lineNumber + int(self.jumpNumber) > self.totalLines or lineNumber + int(self.jumpNumber) < 1:
                print("Out of range")
            else:
                return int(lineNumber + self.jumpNumber - 1)

    def determineTrue(self, compare1, operator, compare2, varDict, compare2kind):
        if self.compare1 in self.varDict:
            self.val1 = varDict[compare1]
        else:
            self.val1 = compare1
        if compare2 in varDict:
            self.val2 = varDict[compare2]  # Corrected syntax
        else:
            if compare2kind is GrinTokenKind.LITERAL_INTEGER:
                self.val2 = int(compare2)
            elif compare2kind is GrinTokenKind.LITERAL_FLOAT:
                self.val2 = float(compare2)
            else:
                self.val2 = compare2


        if operator == '<':  # Corrected comparison operator
            if self.val1 < self.val2:
                return True
        elif operator == '>':
            if self.val1 > self.val2:
                return True
        elif operator == '<=':
            if self.val1 <= self.val2:
                return True
        elif operator == '>=':
            if self.val1 >= self.val2:
                return True
        elif operator == '=':
            if self.val1 == self.val2:
                return True
        elif operator == '<>':
            if self.val1 != self.val2:
                return True
        return False  # Return False if conditions are not met
