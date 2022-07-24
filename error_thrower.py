#  KeyError,
#  AssertionError,
#  AttributeError,
#  EOFError,
#  FloatingPointError,
#  GeneratorExit,
#  ImportError,
#  IndexError,
#  KeyError,
#  KeyboardInterrupt,
#  MemoryError,
#  NameError,
#  NotImplementedError,
#  OSError,
#  OverflowError,
#  ReferenceError,
#  StopIteration,
#  SyntaxError,
#  IndentationError,
#  TabError,
#  SystemError,
#  SystemExit,
#  TypeError,
#  UnboundLocalError,
#  UnicodeError,
#  UnicodeEncodeError,
#  UnicodeDecodeError,
#  UnicodeTranslateError,
#  ValueError,
#  ZeroDivisionError





# REQURE
import itertools
import random

class Error_Objective:
    def __init__(self):
        # TO-DO ( Dashed to allow commit)
        # Add more Exceptions.
        # Optimize Order
        # - Dial, 07/23/2022 9:32 PM EST
        self.current_hardness = "EASY"
        self.HARDNESS = itertools.cycle({"EASY", "MOD", "HARD"})
        self.ERRORS = {"EASY": {"KeyError",
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
                                "FileNotFoundError"
                                },  # "Easy" Exceptions.

                       "MOD": {"MemoryError",
                               "GeneratorExit",
                               "OverflowError",
                               "EOFError",
                               "StopIteration"
                               },  # "Moderate" Exceptions

                       "HARD": {"UnboundLocalError",
                                "UnicodeError",
                                "UnicodeTranslateError",
                                "UnicodeEncodeError",
                                "UnicodeDecodeError",
                                "SystemError",
                                "OSError",
                                "IOError",
                                "NotImplementedError",
                                "NotImplemented",
                                "DeprecationWarning"
                                }

                       }

    def toggle_difficulty_level(self, difficulty_reset: bool = False):
        if difficulty_reset:
            self.current_hardness = self.HARDNESS[0]
        else:
            self.current_hardness = next(self.HARDNESS)
            return self.current_hardness

    def objective(self, amount: int = 1):
        difficulty = self.current_hardness
        try:
            if amount > 1:
                raise UserWarning("This is being removed; objective() will only return one exception per call.")
            else:
                return list(self.ERRORS[difficulty])[random.randint(0, len(self.ERRORS[difficulty])-1)]
        except Exception as err:
            raise Exception(
                f"Something went wrong in '{str(__name__)[2:len(__name__) - 2]},' the Exception in question is {str(type(err))[7:len(str(type(err))) - 1]}. \n The error is as follows: \n {str(err)}")


errors = Error_Objective()
# print(errors.objective())
# errors.toggle_difficulty_level()
