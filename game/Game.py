import asyncio
import random

import fastapi
from fastapi import FastAPI, WebSocket

ERRORS = {
    "SyntaxError",
    "TypeError",
    "ValueError",
    "ModuleNotFoundError",
}  # create a set of errors that must be raised.

app = FastAPI()

task = None


class ErrorGenerator:
    async def evaluate(self, error: str, code: str):
        """Checks if the code provided"""
        if "raise" in code:
            return -69000000, False  # Nice
        else:
            try:
                exec(code)
            except Exception as eval_error:
                if error in str(type(eval_error)):
                    return 1, True
                else:
                    return 0, False
            if "eval_error" not in locals():
                return -1, False


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
            self.game[user] -= abs(points)
        except KeyError:
            raise UserError("User does not exist.")

    async def user(self, user: str):
        """Returns the points for a user."""
        try:
            return self.game[user]
        except KeyError:
            raise UserError("User does not exist.")


game = Game()


@app.websocket("/")
async def root(websocket: WebSocket):
    """This function is called when a websocket connection is made to ws://localhost:8000/ (root of the api)."""
    global game
    evaluation = ErrorGenerator()
    user = None
    await websocket.accept()
    try:
        while True:
            try:
                user = await websocket.receive_text()
                await game.login(user)
            except UserError:
                await websocket.close(403, reason="User already exists")
            else:
                break

        while True:
            cur = ERROR[::]
            await websocket.send_text("Raise error: " + cur)  # Random error is sent.
            code = await websocket.receive_text()
            if code == "--leaderboard":
                string = ""
                c = 1
                for k, v in sorted(game.game.items(), key=lambda value: value[1]):
                    string += f"{c}. {k} - {v}\n"
                    c += 1
                await websocket.send_text(string)
                continue
            elif code.startswith("--test"):
                code = code.lstrip("--test ").lstrip("--test")
                code = await evaluation.evaluate(cur, code)
                await websocket.send_text(code[1])
                continue
            else:
                game.users_submitted += 1
                await asyncio.wait_for(task, timeout=None)
                code = await evaluation.evaluate(cur, code)
                if code[1]:
                    await game.add(user, code[0])
                    await websocket.send_text(
                        f"You passed!! Yay! You gained {code[0]} points and now have {await game.user(user)} points!"
                    )  # vars here

                else:
                    await game.remove(user, code[0])
                    await websocket.send_text(
                        f"Oh no, you did not pass. You lost {code[0]} points and now have {await game.user(user)} points."
                    )  # vars here
    except fastapi.WebSocketDisconnect:  # Gracefully cleanup game and close socket.
        print(f"{user} left the game.")
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
