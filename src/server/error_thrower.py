import random


class Error_Objective:
    def __init__(self):
        # TO-DO ( Dashed to allow commit)
        # Add more Exceptions.
        # Optimize Order
        # - Dial, 07/23/2022 9:32 PM EST
        self.ERRORS = {
            "EASY": {
                "KeyError",
                "AssertionError",
                "ValueError",
                "ZeroDivisionError",
                "KeyboardInterrupt",
                "IndentationError",
                "TypeError",
                "ImportError",
                "AttributeError",
                "SystemExit",
                "IndexError",
                "TabError",
                "ReferenceError",
                "NotADirectoryError",
                "FileNotFoundError",
            },  # "Easy" Exceptions.
            "MOD": {
                "MemoryError",
                "GeneratorExit",
                "OverflowError",
                "EOFError",
                "StopIteration",
            },  # "Moderate" Exceptions
            "HARD": {
                "UnboundLocalError",
                "UnicodeError",
                "UnicodeTranslateError",
                "UnicodeEncodeError",
                "UnicodeDecodeError",
                "SystemError",
                "OSError",
                "IOError",
                "NotImplementedError",
                "NotImplemented",
                "DeprecationWarning",
            },
        }

    def toggle_difficulty_level(self, *args):
        raise DeprecationWarning(
            "toggle_difficulty_level has been removed, please use 'objective(difficulty=...)' "
        )

    def objective(self, difficulty: str = None, amount: int = 1):
        try:
            if difficulty is None:
                raise SyntaxError(
                    "Difficulty is required due to toggle_difficulty_level being removed."
                )

            if amount > 1:
                raise DeprecationWarning(
                    "This is being removed; objective() will only return one exception per call."
                )
            else:
                return list(self.ERRORS[difficulty])[
                    random.randint(0, len(self.ERRORS[difficulty]) - 1)
                ]
        except Exception as err:
            raise Exception(
                f"Something went wrong in '{str(__name__)[2:len(__name__) - 2]},' the Exception in question is {str(type(err))[7:len(str(type(err))) - 1]}. \n The error is as follows: \n {str(err)}"
            )
