import asyncio
import json
import sys

import websockets


async def handle(websocket, resp: dict):
    resp = json.loads(resp)
    if resp["type"] == "error":
        print(resp["data"])
        sys.exit()

    if resp["type"] == "objective":
        print(resp["data"])
        return

    if resp["type"] == "login":
        print(resp["data"])
        return

    if resp["type"] == "submit":
        print(resp["data"])
        await websocket.recv()
        return

    if resp["type"] == "leaderboard":
        c = 1
        for k, v in resp["data"].items():
            print(f"{c}. {k} - {v}")
            c += 1
        return
            
    if resp['type'] == 'login':
        print(resp['data'])
        return

    else:
        print(f"Unsupported response type - {resp['type']}")
        await websocket.close()
        sys.exit()


async def main():
    async with websockets.connect("ws://localhost:8000") as socket:
        user = input("Enter username: ")
        await socket.send(json.dumps({"type": "register", "data": user}))
        await handle(socket, await socket.recv())
        await socket.recv()
        while socket.open:
            await handle(socket, await socket.recv())
            inputted = input(":")
            if inputted == "--leaderboard":
                await socket.send(json.dumps({"type": "leaderboard"}))
            if inputted == "--close":
                await socket.close()
            else:
                await socket.send(json.dumps({"type": "submit", "data": inputted}))
            await handle(socket, await socket.recv())


asyncio.run(main())
