import asyncio

from user import User
from error_thrower import Error_Objective


"""
Copyright 2021 Python Discord
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

"""
|========================================|
|PLEASE NOTIFY ME (DIAL) BEFORE CHANGING!|
|            ALSO MAKE A COPY!!          |
|========================================|
"""


class PointHandlerError(Exception):
    """Raised when an exception occurs inside PointHandler"""
    __module__ = "builtins"


class PointHandler:
    """Handles point gain in terms of difficulty."""

    async def point(self, assignment: str, client_user: User, error_obj: Error_Objective = Error_Objective()):
        """
        async awaits objective_checker(...) to return an int.
        if the integer returned is in range of the # of keys in ERROR; the score will be appended with the returned-int.

        Raises PointHandlerError from ValueError if outside the range.
        Raises PointHandlerError on any exception.
        """

        try:
            difficulty_int: int = await self.objective_checker(assignment)
            if difficulty_int in range(len(error_obj.ERRORS)):
                client_user.score += difficulty_int
            else:
                raise ValueError(f"Difficulty must be an int with the range of 1 to {len(error_obj)}")
            return client_user.score
        except BaseException as exception:
            raise PointHandlerError(
                f" \n Type: {str(type(exception))[7:len(str(type(exception))) - 1]} \n \n Reason: {exception}")

    @staticmethod
    async def objective_checker(assignment: str, error_obj: Error_Objective = Error_Objective()):
        """Comment needed."""

        try:
            for x in error_obj.ERRORS:
                for y in error_obj.ERRORS[x]:
                    if assignment == y:
                        return x
                    else:
                        continue
            raise PointHandlerError(f"{assignment} not found")
        except BaseException as exception:
            raise PointHandlerError(
                f" \n Type: {str(type(exception))[7:len(str(type(exception))) - 1]} \n \n Reason: {exception}")


pointhandle = PointHandler()
foo = asyncio.run(pointhandle.point("ValueError", User("Bob")))
print(foo)
"""
|========================================|
|PLEASE NOTIFY ME (DIAL) BEFORE CHANGING!|
|            ALSO MAKE A COPY!!          |
|========================================|
"""
