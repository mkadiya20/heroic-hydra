import fastapi
from error_thrower import Error_Objective
from fastapi import FastAPI, WebSocket

from Game import Game

error_obj = Error_Objective()


game = Game()
app = FastAPI()
clients: dict[str, WebSocket] = {}


async def register_user(username: str, websocket: WebSocket):
    """Registers a user with the server if the username is not already taken"""
    if username not in clients.keys():
        await game.login(username)
        clients[username] = websocket
    else:
        await websocket.send_json({"type": "error", "data": "Username already taken"})
        await websocket.close()


async def get_leaderboard(websocket: WebSocket):
    """Returns the leaderboard"""
    await websocket.send_json(
        {"type": "leaderboard", "data": await game.get_leaderboard()}
    )


async def submit(websocket: WebSocket, code: str, user: str, error: str):
    """Submits user code to Game.Game object for submission and evaluation."""
    code = code.replace("'", '"')
    print(code)
    result = await game.submit(user, code)
    # print(result)
    await websocket.send_json(
        {
            "type": "submit",
            "data": "Your code raised the error provided!"
            if result
            else "Your code did not raise the error provided.",
        }
    )


@app.websocket("/")
async def root(websocket: WebSocket):
    """This function is called when a websocket connection is made to http://localhost:8000/"""
    try:
        await websocket.accept()

        data = await websocket.receive_json()

        match data["type"]:
            case "register":
                user = data["data"]
                await register_user(user, websocket)
                await websocket.send_json(
                    {"type": "login", "data": f"Logged in as {user}!"}
                )
                print(f"{user} joined the game.")

            case _:
                await websocket.send_json(
                    {"type": "error", "data": "Register user first."}
                )
                await websocket.close()

        while True:

            error = error_obj.objective()
            await game.new_target(user, error)
            while True:
                await websocket.send_json(
                    {"type": "objective", "data": f"Produce error {error}."}
                )
                data = await websocket.receive_json()
                match data["type"]:
                    case "leaderboard":
                        await get_leaderboard(websocket)

                    case "submit":
                        await submit(websocket, data["data"], user, error)
                        break

                    case "logout":
                        await websocket.close()

                    case _ as err:
                        await websocket.send_json(
                            {
                                "type": "error",
                                "data": f"Unsupported request type - {err}",
                            }
                        )
                        await websocket.close()

    except fastapi.WebSocketDisconnect:
        try:
            await game.logout(user)
            del clients[user]
            print(f"{user} left the game")
        except UnboundLocalError:
            pass
