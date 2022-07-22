from fastapi import FastAPI, WebSocket
import functools
import inspect

app = FastAPI()


def force(func):
    """
    Forces annotation on arguments of functions. Not to be used with annotations from typing library, or with indexes like 'list[int]'
    """
    sig = inspect.signature(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        bound_arguments = sig.bind(*args, **kwargs).arguments
        c = dict()
        for i, v in sig.parameters.items():
            if v.kind == v.POSITIONAL_OR_KEYWORD:
                if v.annotation != v.empty:
                    if not (isinstance(bound_arguments[v.name], v.annotation)):
                        c[v.name] = v.annotation(bound_arguments[v.name])
                    else:
                        c[v.name] = bound_arguments[v.name]
                else:
                    c[v.name] = bound_arguments[v.name]
            else:
                c[v.name] = bound_arguments[v.name]
        return func(**c)

    return


class Game:
    class UserError(Exception):
        """Is used to represent errors with users."""

        pass

    """Represents a game, a instantiate this class to get the game started."""

    def __init__(self) -> None:
        self.game = {}

    @force
    async def login(self, user: str) -> None:
        """Adds a user to the game."""
        if user not in self.game.keys():
            self.game[user] = 0
        else:
            raise self.UserError("User already exists.")

    @force
    async def logout(self, user: str) -> None:
        """Removes a user to the game."""
        if user in self.game.keys():
            del self.game[user]
        else:
            raise self.UserError("User already does not exist.")

    @force
    async def add(self, user: str, points: int) -> None:
        """Adds points to a user."""
        try:
            self.game[user] += points
        except KeyError:
            raise self.UserError("User does not exist.")

    @force
    async def remove(self, user: str, points: int) -> None:
        """Deducts points from a user."""
        try:
            self.game[user] -= points
        except KeyError:
            raise self.UserError("User does not exist.")

    @force
    async def user(self, user: str):
        """Returns the points for a user."""
        try:
            return self.game[user]
        except KeyError:
            raise self.UserError("User does not exist.")


@app.websocket("/")
async def root(websocket: WebSocket):
    """This function is called when a websocket connection is made to http://localhost:8000/ (root of the api)."""
    await websocket.accept()

    while True:
        data = await websocket.receive_text()  # noqa F841
        # using the submission classes, check if data is valid.
        code = -69000000000, True
        if code[1]:
            await websocket.send_text(
                "You passed!! Yay! You gained {code[0]} points and now have {new_points}!"
            )  # vars here
        else:
            await websocket.send_text(
                "Oh no, you did not pass. You lost {code[0]} points and now have {new_points}."
            )  # vars here
