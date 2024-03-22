from grin import GrinTokenKind


# Variables, location, and stack in processor

class BaseHolder:
    """Base class defining the execute method.

    Subclasses must implement the execute() method.
    """

    def execute(self, lineNumber):
        """Method to be implemented by subclasses.

        Args:
            lineNumber (int): The line number.
        """
        raise NotImplementedError("Subclasses must implement execute()")


class Let(BaseHolder):
    """Class representing the 'LET' operation.

    This operation either assigns a value to a variable or updates an existing variable's value.
    """

    def __init__(self, variableDict, key, value, kind):
        """
        Args:
            variableDict (dict): Dictionary containing variables and their values.
            key (str): The variable to be updated or created.
            value (str): The value to be assigned to the variable.
            kind (GrinTokenKind): The type of token for the value.
        """
        self.varDict = variableDict
        self.key = key
        self.value = value
        self.kind = kind

    def execute(self, lineNumber):
        """Execute the 'LET' operation.

        This method executes the 'LET' operation based on the provided parameters.

        Args:
            lineNumber (int): The line number.
        """
        if self.value in self.varDict: #Ex: LET A B (B already exists)
            self.varDict[self.key] = self.varDict[self.value]
        elif self.kind is GrinTokenKind.IDENTIFIER: #Ex: LET A B (B doesn't exist)
            self.varDict[self.value] = 0
            self.varDict[self.key] = self.varDict[self.value]
        else: #LET A 3 (existence doesn't matter)
            self.varDict[self.key] = self.value

class Print(BaseHolder):
    """A class to handle printing of variables or values."""

    def __init__(self, variableDict, key, kind):
        """
        Initializes a Print object.

        Args:
        - variableDict (dict): A dictionary containing variables.
        - key (str): The key to access a variable in variableDict or a value to print.
        - kind: The type or kind of the key (assuming GrinTokenKind is defined elsewhere).
        """
        self.varDict = variableDict
        self.key = key
        self.kind = kind
        self.toPrint = 0

    def execute(self, lineNumber):
        """
        Executes the printing operation based on the stored key, value, or identifier.

        Args:
        - lineNumber (int): The line number associated with the execution.

        Prints:
        - The value of the key in variableDict, 0 if the key doesn't exist,
          or the key itself if it's not present in variableDict and not of type identifier.
        """
        # Check if self.key is in var dict
        if self.key in self.varDict:
            self.toPrint = self.varDict[self.key]
        elif self.kind is GrinTokenKind.IDENTIFIER:
            self.varDict[self.key] = 0
            self.toPrint = 0
        else:
            self.toPrint = self.key
        print(self.toPrint)