from error_thrower import Error_Objective
from user import User

error_obj = Error_Objective()


class UserError(Exception):
    """Is used to represent errors with users."""


class Game:
    """Represents a game, a instantiate this class to get the game started."""

    def __init__(self) -> None:
        self.users = {}
        self.users_submitted = 0

    async def login(self, username: str) -> None:
        """Adds a user to the game."""
        if username not in self.users.keys():
            self.users[username] = User(username)
        else:
            raise UserError("User already exists.")

    async def logout(self, username: str) -> None:
        """Removes a user from the game."""
        if username in self.users.keys():
            del self.users[username]
        else:
            raise UserError("User does not exist.")

    async def submit(self, username: str, submission_str: str) -> None:
        """Evaluates the user's submission and changes their score"""
        if username in self.users.keys():
            self.users[username].submit(submission_str)
        else:
            raise UserError("User does not exist.")

    async def user_score(self, username: str):
        """Returns the points for a user."""
        try:
            return self.users[username].score
        except KeyError:
            raise UserError("User does not exist.")

    async def new_target(self, username: str):
        """Updates the user's target error"""
        try:
            new_error = error_obj.objective()
            self.users[username].assign_objective(new_error)
        except KeyError:
            raise UserError("User does not exist.")

    async def get_leaderboard(self):
        """Returns the leaderboard"""
        string = ""
        c = 1
        for k, v in self.users.items():
            string += "{c}. {k} - {v.points} \n"
            c += 1
        return string
