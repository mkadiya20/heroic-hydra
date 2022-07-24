"""
Copyright 2021 Python Discord
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import random


class DifficultyObjectivesCompleted(Exception):
    """Raised when all objectives in self.ERROR[difficulty] is exactly equal to already_used_keywords."""

    __module__ = "builtins"
    # pass


class AllObjectivesCompleted(Exception):
    """Raised when all objectives in self.ERROR is exactly equal to already_used_keywords."""

    __module__ = "builtins"
    # raise NotImplementedError  # Currently Unused this should go in __init__ I assume - barko


class Error_Objective:
    """Master Class for Error Objective Calling."""

    def __init__(self):
        # TO-DO ( Dashed to allow commit)
        # Add more Exceptions.
        # Optimize Order
        # - Dial, 07/23/2022 9:32 PM EST
        self.UNUSED_ERRORS = {
            "NotImplementedError",
            "PendingDeprecationWarning",
            "FloatingPointError",
            "StopAsyncIteration",
            "Exception",
            "BufferError",
            "LookupError",
            "BaseException",
        }  # UNUSED / BASECLASS / REQUIRE "RAISE" https://docs.python.org/3/library/exceptions.html#built-in-exceptions

        self.ERRORS = {
            "EASY": {
                "IndexError",
                "KeyError",
                "TypeError",
                "AttributeError",
                "ZeroDivisionError",
                "ValueError",
                "AssertionError",
                "OverflowError",
                "OSError",
                "NameError",
                "IndentationError",
                "TabError",
                "IOError",
                "ImportError",
                "KeyboardInterrupt",
                "SyntaxError",
                "SystemExit",
                "UnboundLocalError",
                "LookupError",
                "EOFError",
                "RecursionError",
            },  # "Easy" Exceptions.
            "MOD": {
                "GeneratorExit",
                "StopIteration",
                "MemoryError",
                "StopIteration",
                "UnicodeError",
                "UnicodeEncodeError",
                "UnicodeDecodeError",
                "DeprecationWarning",
            },  # "Moderate" Exceptions
            "HARD": {
                "SystemError",
                "EnvironmentError",
                "RuntimeError",
                "BufferError",
            },  # "Hard" Exceptions
        }

    def objective(self, difficulty: str, already_used_keywords: list | tuple = None):
        try:
            if not already_used_keywords:
                return list(self.ERRORS[difficulty])[
                    random.randint(0, len(self.ERRORS[difficulty]) - 1)
                ]
            else:
                for x in self.ERRORS[difficulty]:
                    choice = list(self.ERRORS[difficulty])[
                        random.randint(0, len(self.ERRORS[difficulty]) - 1)
                    ]
                    if choice not in already_used_keywords:
                        return choice
                    else:
                        continue
                counter = 0
                for x in self.ERRORS[difficulty]:
                    for y in already_used_keywords:
                        if x == y:
                            counter += 1
                        else:
                            continue
                if counter == len(self.ERRORS[difficulty]):
                    raise DifficultyObjectivesCompleted(
                        f"All Objectives in {difficulty} are completed."
                    )

        except DifficultyObjectivesCompleted:
            raise DifficultyObjectivesCompleted(
                f"All Objectives in {difficulty} are completed."
            )

        except Exception as err:
            raise Exception(
                f"Something went wrong in '{str(__name__)[2:len(__name__) - 2]},' the Exception in question is {str(type(err))[7:len(str(type(err))) - 1]}. \n The error is as follows: \n {str(err)}"
            )
