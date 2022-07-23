import random


class Error_Objective:
    def __init__(self):
        self.ERRORS = [
            "KeyError",
            "AssertionError",
            "AttributeError",
            "EOFError",
            "FloatingPointError",
            "GeneratorExit",
            "ImportError",
            "IndexError",
            "KeyError",
            "KeyboardInterrupt",
            "MemoryError",
            "NameError",
            "NotImplementedError",
            "OSError",
            "OverflowError",
            "ReferenceError",
            "StopIteration",
            "SyntaxError",
            "IndentationError",
            "TabError",
            "SystemError",
            "SystemExit",
            "TypeError",
            "UnboundLocalError",
            "UnicodeError",
            "UnicodeEncodeError",
            "UnicodeDecodeError",
            "UnicodeTranslateError",
            "ValueError",
            "ZeroDivisionError",
        ]

    def objective(self, amount: int = 1):
        """Get the error objective"""
        try:
            if amount > 1:
                return random.sample(self.ERRORS, amount)
            else:
                return random.choice(self.ERRORS)
        except Exception as err:
            raise Exception(
                f"Something went wrong in '{str(__name__)[2:len(__name__) - 2]},' the Exception in question is {str(type(err))[7:len(str(type(err))) - 1]}. \n The error is as follows: \n {str(err)}"
            )
