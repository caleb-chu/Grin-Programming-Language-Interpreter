from grin import processor, BaseHolder


class INNUM(BaseHolder):
    def __init__(self, var, value, myDict):
        self._var = var
        self._value = value
        self._myDict = myDict

    def execute(self, lineNumber):
        try:
            myVal = int(self._value)
            self._myDict[self._var] = myVal
        except ValueError:
            try:
                myVal = float(self._value)
                self._myDict[self._var] = myVal
            except ValueError:
                print("Please enter a valid integer or float")


class INSTR(BaseHolder):
    def __init__(self, var, value, myDict):
        self._var = var
        self._value = value
        self._myDict = myDict

    def execute(self, lineNumber):
        tempValue = str(self._value)
        self._myDict[self._var] = tempValue