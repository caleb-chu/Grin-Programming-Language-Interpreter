from grin import GrinTokenKind

class ADD:
    """Class for performing addition operation."""
    def __init__(self, myDict, addVar1, addVar2, varKind1, varKind2):
        """Initialize ADD class attributes.

        Args:
        - myDict: Dictionary containing variables and their values.
        - addVar1: Name of the first variable or value.
        - addVar2: Name of the second variable or value.
        - varKind1: Kind of the first variable (identifier, literal integer, literal float).
        - varKind2: Kind of the second variable (identifier, literal integer, literal float).
        """
        self.myDict = myDict
        self.addVar1 = addVar1
        self.addVar2 = addVar2
        self.varKind1 = varKind1
        self.varKind2 = varKind2
        self.first = 0
        self.second = 0
    #ADD A B works, 0 + 0 is 0
    def execute(self,lineNumber):
        if self.addVar1 in self.myDict: #Var1 is in dictionary
            self.first = self.myDict[self.addVar1]
        else: #Var1 is not in dictionary
            self.myDict[self.addVar1] = 0
            self.first = self.myDict[self.addVar1]

        if self.addVar2 in self.myDict: #Var 2 is in dictionary
            self.second = self.myDict[self.addVar2]
        elif self.varKind2 is GrinTokenKind.IDENTIFIER: #Var 2 is variable but not in dictionary
            self.myDict[self.addVar2] = 0
            self.second = self.myDict[self.addVar2]
        else: #not a variable
            if self.varKind2 is GrinTokenKind.LITERAL_INTEGER:
                self.second = int(self.addVar2)
            elif self.varKind2 is GrinTokenKind.LITERAL_FLOAT:
                self.second = float(self.addVar2)
            else:
                self.second = self.addVar2

        try:
            self.myDict[self.addVar1] = self.first + self.second
        except Exception as e:
            print(f"cannot add string with a float/integer {e}")

class SUB:
    """Class for performing subtraction operation."""
    def __init__(self, myDict, addVar1, addVar2, varKind1, varKind2):
        """Initialize SUB class attributes.

        Args:
        - myDict: Dictionary containing variables and their values.
        - addVar1: Name of the first variable or value.
        - addVar2: Name of the second variable or value.
        - varKind1: Kind of the first variable (identifier, literal integer, literal float).
        - varKind2: Kind of the second variable (identifier, literal integer, literal float).
        """
        self.myDict = myDict
        self.addVar1 = addVar1
        self.addVar2 = addVar2
        self.varKind1 = varKind1
        self.varKind2 = varKind2
        self.first = 0
        self.second = 0
    #ADD A B works, 0 + 0 is 0
    def execute(self,lineNumber):
        if self.addVar1 in self.myDict: #Var1 is in dictionary
            self.first = self.myDict[self.addVar1]
        else: #Var1 is not in dictionary
            self.myDict[self.addVar1] = 0
            self.first = self.myDict[self.addVar1]

        if self.addVar2 in self.myDict: #Var 2 is in dictionary
            self.second = self.myDict[self.addVar2]
        elif self.varKind2 is GrinTokenKind.IDENTIFIER: #Var 2 is variable but not in dictionary
            self.myDict[self.addVar2] = 0
            self.second = self.myDict[self.addVar2]
        else: #not a variable
            if self.varKind2 is GrinTokenKind.LITERAL_INTEGER:
                self.second = int(self.addVar2)
            elif self.varKind2 is GrinTokenKind.LITERAL_FLOAT:
                self.second = float(self.addVar2)
            else:
                self.second = self.addVar2

        try:
            self.myDict[self.addVar1] = self.first - self.second
        except Exception as e:
            print(f"cannot subtract strings {e}")

class MULT:
    """Class for performing multiplication operation."""
    def __init__(self, myDict, addVar1, addVar2, varKind1, varKind2):
        """Initialize MULT class attributes.

        Args:
        - myDict: Dictionary containing variables and their values.
        - addVar1: Name of the first variable or value.
        - addVar2: Name of the second variable or value.
        - varKind1: Kind of the first variable (identifier, literal integer, literal float).
        - varKind2: Kind of the second variable (identifier, literal integer, literal float).
        """
        self.myDict = myDict
        self.addVar1 = addVar1
        self.addVar2 = addVar2
        self.varKind1 = varKind1
        self.varKind2 = varKind2
        self.first = 0
        self.second = 0
    #ADD A B works, 0 + 0 is 0
    def execute(self,lineNumber):
        if self.addVar1 in self.myDict: #Var1 is in dictionary
            self.first = self.myDict[self.addVar1]
        else: #Var1 is not in dictionary
            self.myDict[self.addVar1] = 0
            self.first = self.myDict[self.addVar1]

        if self.addVar2 in self.myDict: #Var 2 is in dictionary
            self.second = self.myDict[self.addVar2]
        elif self.varKind2 is GrinTokenKind.IDENTIFIER: #Var 2 is variable but not in dictionary
            self.myDict[self.addVar2] = 0
            self.second = self.myDict[self.addVar2]
        else: #not a variable
            if self.varKind2 is GrinTokenKind.LITERAL_INTEGER:
                self.second = int(self.addVar2)
            elif self.varKind2 is GrinTokenKind.LITERAL_FLOAT:
                self.second = float(self.addVar2)
            else:
                self.second = self.addVar2


        try:
            self.myDict[self.addVar1] = self.first * self.second
        except Exception as e:
            print(f"can only multiply strings with ints{e}")

class DIV:
    """Class for performing division operation."""
    def __init__(self, myDict, addVar1, addVar2, varKind1, varKind2):
        """Initialize Division class attributes.

        Args:
        - myDict: Dictionary containing variables and their values.
        - addVar1: Name of the first variable or value.
        - addVar2: Name of the second variable or value.
        - varKind1: Kind of the first variable (identifier, literal integer, literal float).
        - varKind2: Kind of the second variable (identifier, literal integer, literal float).
        """
        self.myDict = myDict
        self.addVar1 = addVar1
        self.addVar2 = addVar2
        self.varKind1 = varKind1
        self.varKind2 = varKind2
        self.first = 0
        self.second = 0
    #ADD A B works, 0 + 0 is 0
    def execute(self,lineNumber):
        if self.addVar1 in self.myDict: #Var1 is in dictionary
            self.first = self.myDict[self.addVar1]
        else: #Var1 is not in dictionary
            self.myDict[self.addVar1] = 0
            self.first = self.myDict[self.addVar1]

        if self.varKind1 is GrinTokenKind.LITERAL_INTEGER:
            self.first = int(self.first)
        elif self.varKind1 is GrinTokenKind.LITERAL_FLOAT:
            self.first = float(self.first)

        if self.addVar2 in self.myDict: #Var 2 is in dictionary
            self.second = self.myDict[self.addVar2]
        elif self.varKind2 is GrinTokenKind.IDENTIFIER: #Var 2 is variable but not in dictionary
            self.myDict[self.addVar2] = 0
            self.second = self.myDict[self.addVar2]
        else:
            if self.varKind2 is GrinTokenKind.LITERAL_INTEGER:
                self.second = int(self.addVar2)
            elif self.varKind2 is GrinTokenKind.LITERAL_FLOAT:
                self.second = float(self.addVar2)
            else:
                self.second = self.addVar2

        if self.varKind2 is GrinTokenKind.LITERAL_INTEGER:
            self.second = int(self.addVar2)
        elif self.varKind2 is GrinTokenKind.LITERAL_FLOAT:
            self.second = float(self.addVar2)

        try:
            if self.first is int and self.second is int:
                self.myDict[self.addVar1] = self.first // self.second
            else:
                self.myDict[self.addVar1] = self.first / self.second
        except Exception as e:
            print(f"cannot divide with strings {e}")