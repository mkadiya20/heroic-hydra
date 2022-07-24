import asyncio
import json
import sys

import websockets


async def handle(websocket, resp: dict):
    resp = json.loads(resp)
    match resp["type"]:
        case "error":
            print(resp["error"])
            sys.exit()

        case "text":
            print(resp["text"])

        case _ as err:
            print(f"Unsupported response type - {err}")


async def main():
    async with websockets.connect("ws://localhost:8000") as socket:
        user = input("Enter username: ")
        await socket.send(json.dumps({"type": "register", "data": user}))
        await handle(socket, await socket.recv())
        while True:
            await handle(socket, await socket.recv())
            inputted = input(":")
            if inputted == "--leaderboard":
                await socket.send(json.dumps({"type": "leaderboard"}))
            if inputted.startswith("--test"):
                await socket.send(
                    json.dumps(
                        {
                            "type": "test",
                            "data": inputted.lstrip("--test ").lstrip("--test"),
                        }
                    )
                )
            if inputted == "--close":
                await socket.close()
            else:
                await socket.send(json.dumps({"type": "submission", "data": inputted}))
            await handle(socket, await socket.recv())


asyncio.run(main())
