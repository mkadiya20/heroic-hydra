import asyncio

from user import User
from error_thrower import Error_Objective


class PointHandlerError(Exception):
    """Raised when an exception occurs inside PointHandler"""
    __module__ = "builtins"


class PointHandler:

    async def point(self, assignment: str, client_user: User):
        try:
            match await self.objective_checker(assignment):
                case 1:
                    client_user.score += 1
                case 2:
                    client_user.score += 1
                case 3:
                    client_user.score += 1
                case _:
                    raise ValueError("Difficulty must be an int with the range of 1 to 3.")
            return client_user.score
        except BaseException as exception:
            raise PointHandlerError(
                f" \n Type: {str(type(exception))[7:len(str(type(exception))) - 1]} \n \n Reason: {exception}")

    async def objective_checker(self, assignment: str, error_obj: Error_Objective = Error_Objective()):
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
