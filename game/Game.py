import asyncio
import random

import fastapi
from fastapi import FastAPI, WebSocket

ERRORS = {
    "TypeError: can't concat str to bytes."
}  # create a set of errors that must be raised.

app = FastAPI()

task = None


class UserError(Exception):
    """Is used to represent errors with users."""

    pass


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
            self.game[user] -= points
        except KeyError:
            raise UserError("User does not exist.")

    async def user(self, user: str):
        """Returns the points for a user."""
        try:
            return self.game[user]
        except KeyError:
            raise UserError("User does not exist.")


game = Game()


@app.get("/leaderboard")
async def leaderboard():
    """Returns the points for a single user if passed, else the whole leaderboard."""
    string = ""
    c = 1
    for k, v in sorted(game.game.items(), key=lambda value: value[1]):
        string += f"{c}. {k} - {v}"
        c += 1
    return string


@app.websocket("/")
async def root(websocket: WebSocket):
    global game
    """This function is called when a websocket connection is made to ws://localhost:8000/ (root of the api)."""
    try:
        await websocket.accept()

        while True:
            try:
                await websocket.send_text("Enter username")

                user = await websocket.receive_text()

                await game.login(user)
            except UserError:
                await websocket.send_text("ERROR")
            else:
                await websocket.send_text("Login successful")
                break

        while True:
            await websocket.send_text(
                f"You must produce error {ERROR}"
            )  # Random error is sent.
            code = await websocket.receive_text()
            del code
            game.users_submitted += 1
            asyncio.wait_for(task, timeout=None)
            #  The code above
            #  Using the submission classes, check if the code raises the error expected.
            #  I'm not going to implement ice wolfy's submission class here, as the server and client are both sending strings atm while submissions take files.
            code = (-69000000000, False)
            if code[1]:
                await websocket.send_text(
                    "You passed!! Yay! You gained {code[0]} points and now have {new_points}!"
                )  # vars here
            else:
                await websocket.send_text(
                    "Oh no, you did not pass. You lost {code[0]} points and now have {new_points}."
                )  # vars here
    except fastapi.WebSocketDisconnect:  # Gracefully cleanup game and close socket.
        await game.logout(user)
        game.users_submitted -= 1


async def loop():
    """Represents when all users have submitted code."""
    global ERROR
    ERROR = random.choice(tuple(ERRORS))
    while True:
        if len(game.game.items()) == game.users_submitted:
            game.users_submitted = 0
            break
        else:
            await asyncio.sleep(0.1)


async def main():
    """Just creates tasks."""
    global task
    while True:
        task = asyncio.create_task(loop())
        await asyncio.wait([task])
        task.cancel()
        await asyncio.sleep(0.1)


event_loop = asyncio.get_event_loop()
asyncio.ensure_future(main())
