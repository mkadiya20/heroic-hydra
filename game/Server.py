import asyncio
import random

import fastapi
from fastapi import FastAPI, WebSocket
from Submissions_str import ErrorGenerator

from Game import Game, UserError

ERRORS = {
    "KeyError",
    "AssertionError",
    "AttributeError",
    "EOFError",
    "FloatingPointError",
    "GeneratorExit",
    "ImportError",
    "IndexError",
    "KeyError",
    "KeyboardInterrupt",
    "MemoryError",
    "NameError",
    "NotImplementedError",
    "OSError",
    "OverflowError",
    "ReferenceError",
    "StopIteration",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "SystemExit",
    "TypeError",
    "UnboundLocalError",
    "UnicodeError",
    "UnicodeEncodeError",
    "UnicodeDecodeError",
    "UnicodeTranslateError",
    "ValueError",
    "ZeroDivisionError",
}  # create a set of errors that must be raised.

app = FastAPI()

task = None

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
                print(f"{user} has joined the game.")
                break

        while True:
            cur = ERROR[::]
            await websocket.send_text("Raise error: " + cur)  # Random error is sent.
            code = await websocket.receive_text()

            async def eval(code):
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
            elif code.startswith("--file"):
                code = code.lstrip("--file ").lstrip("--file")
                async with open(code, "r") as file:
                    dat = file.read()
                code = dat[::]
                await eval(code)
            else:
                game.users_submitted += 1
                await asyncio.wait_for(task, timeout=None)
                code = await evaluation.evaluate(cur, code)
                await eval(code)

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
