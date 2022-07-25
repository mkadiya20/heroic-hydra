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

    async def objective(self, amount: int = 1):
        """Get the error objective"""
        return random.choice(self.ERRORS)
