import asyncio
from user import User, MOD_THRESH, HARD_THRESH

"""
        888                    
        888                    
        888                    
.d8888b 888888 .d88b. 88888b.  
88K     888   d88""88b888 "88b 
"Y8888b.888   888  888888  888 
     X88Y88b. Y88..88P888 d88P 
 88888P' "Y888 "Y88P" 88888P"  
                      888      
                      888      
                      888      
                      
Don't use yet. Not Finished nor tested.
- Dial


"""



class PointManagerError(Exception):
    """Raised when an exception occurs in PointManager"""
    __module__ = "builtins"


class PointMathError(Exception):
    """Raised when a math function fails."""
    __module__ = "PointManagerError"


class PointManager:

    @staticmethod
    async def solve_time_score(local_user: User, solve_time: int):
        try:
            match solve_time:
                case range(0, 2):
                    local_user.score += 3
                case range(3, 4):
                    local_user.score += 2
                case _:
                    local_user.score += 1
        except BaseException as err:
            raise PointMathError(
                f"Type: {str(type(err))[7:len(str(type(err))) - 1]} \n \n Cause: {err.__cause__} \n \n Message: {err}")
        return 0

    @staticmethod
    async def account_for_difficulty(local_user: User):
        try:
            if HARD_THRESH <= local_user.score:
                local_user.score += 3
            elif HARD_THRESH > local_user.score >= MOD_THRESH:
                local_user.score += 2
            else:
                local_user.score += 1
        except BaseException as err:
            raise PointMathError(
                f"Type: {str(type(err))[7:len(str(type(err))) - 1]} \n \n Cause: {err.__cause__} \n \n Message: {err}")
        return 0

    async def point(self, local_user: User, solve_time_seconds: int):
        try:
            await self.account_for_difficulty(local_user)
            await self.solve_time_score(local_user, solve_time_seconds)
        except BaseException as err:
            raise PointManagerError(
                f"Type: {str(type(err))[7:len(str(type(err))) - 1]} \n \n Cause: {err.__cause__} \n \n Message: {err}")

