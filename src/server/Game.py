from user import User


class UserError(Exception):
    """Is used to represent errors with users."""


class Game:
    """Represents a game, a instantiate this class to get the game started."""

    def __init__(self):
        self.users = {}

    async def login(self, username: str):
        """Adds a user to the game."""
        if username not in self.users.keys():
            self.users[username] = User(username)
        else:
            raise UserError("User already exists.")

    async def logout(self, username: str):
        """Removes a user from the game."""
        if username in self.users.keys():
            del self.users[username]
        else:
            raise UserError("User does not exist.")

    async def submit(self, username: str, submission_str: str) -> None:
        """Evaluates the user's submission and changes their score"""
        if username in self.users.keys():
            return await (self.users[username]).submit(submission_str)
        else:
            raise UserError("User does not exist.")

    async def user_score(self, username: str) -> int:
        """Returns the points for a user."""
        try:
            return self.users[username].score
        except KeyError:
            raise UserError("User does not exist.")

    async def new_target(self, username: str) -> str:
        """Updates the user's target error"""
        try:
            return await self.users[username].assign_objective()
        except KeyError:
            raise UserError("User does not exist.")

    async def get_leaderboard(self) -> dict:
        """Returns the leaderboard"""
        return dict(
            sorted(
                ((k, v.score) for k, v in self.users.items()),
                key=(lambda x: x[1]),
                reverse=True,
            )
        )
