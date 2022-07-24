import json

from fastapi import FastAPI, WebSocket
from submission import Submission

# errors = {*json.load(open("errors.json"))}

app = FastAPI()
# submission = Submission()

clients: dict[str, WebSocket] = {}


async def register_user(username: str, websocket: WebSocket):
    """Registers a user with the server if the username is not already taken"""
    if username not in clients:
        clients[username] = websocket
        await websocket.send_text(f"Welcome! You are registered as {username}")
    else:
        await websocket.send_text("Username already taken")
        await websocket.close()


async def get_leaderboard():
    """Returns the leaderboard"""
    pass


@app.websocket("/")
async def root(websocket: WebSocket):
    """This function is called when a websocket connection is made to http://localhost:8000/"""
    await websocket.accept()

    while True:
        data = await websocket.receive_json()

        if data["type"] == "register":
            await register_user(data["username"], websocket)

        elif data["type"] == "leaderboard":
            await get_leaderboard()

        elif data["type"] == "submission":
            submission = Submission(data["data"])
            # TODO: check if submission is valid
            await submission.check_submission(data["data"])
