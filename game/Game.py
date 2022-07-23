class UserError(Exception):

    """Is used to represent errors with users."""


class Game:
    """Represents a game, a instantiate this class to get the game started."""

    def __init__(self) -> None:
        self.game = {}
        self.users_submitted = 0

    async def login(self, user: str) -> None:
        """Adds a user to the game."""
        if user not in self.game.keys():
            self.game[user] = 0
        else:
            raise UserError("User already exists.")

    async def logout(self, user: str) -> None:
        """Removes a user to the game."""
        if user in self.game.keys():
            del self.game[user]
        else:
            raise UserError("User already does not exist.")

    async def add(self, user: str, points: int) -> None:
        """Adds points to a user."""
        try:
            self.game[user] += points
        except KeyError:
            raise UserError("User does not exist.")

    async def remove(self, user: str, points: int) -> None:
        """Deducts points from a user."""
        try:
            self.game[user] -= abs(points)
        except KeyError:
            raise UserError("User does not exist.")

    async def user(self, user: str):
        """Returns the points for a user."""
        try:
            return self.game[user]
        except KeyError:
            raise UserError("User does not exist.")
