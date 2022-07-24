import json
import asyncio
import sys

import websockets

LOOP = asyncio.new_event_loop()


async def listener():
    """Listens for data sent from the server. Then dispatches the event."""
    async with websockets.connect("ws://localhost:8000") as socket:
        while socket.open:
            data = await socket.recv()

            match json.loads(data)["type"]:
                case "error":
                    print(data["data"])
                case "leaderboard":  # Error
                    LOOP.create_task(show_lb(data["data"]))
                case "test":  # Leaderboard
                    print(data["message"])
                case "submit":
                    print(data["message"])
                case "objective":
                    print(data["message"])


async def show_lb(data: dict[str, int]):
    # TODO: hook up with GUI
    print(data)


async def main():
    """Main async function."""
    async with websockets.connect("ws://localhost:8000") as socket:
        try:
            usr = input("Username: ")
            await socket.send(json.dumps({"type": "register", "data": usr}))
            while True:
                dat = await socket.recv()
                print(dat)
                code = input(
                    "Enter code or (--leaderboard to see players, --close to exit, --test to test if code raises error specified): "
                )
                if code == "--close":
                    await socket.close()
                    sys.exit()
                await socket.send(json.dumps({"type": code[2:]}))
                dat = await socket.recv()
                print(dat)
        except KeyboardInterrupt:
            pass

asyncio.set_event_loop(LOOP)
LOOP.create_task(main())
LOOP.run_forever()
