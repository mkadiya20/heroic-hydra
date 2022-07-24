import json
import asyncio
import sys

import websockets


async def main():
    """Main async function."""
    async with websockets.connect("ws://localhost:8000") as socket:
        try:
            usr = input("Username: ")
            await socket.send(json.dumps({"type": "register", "username": usr}))
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


asyncio.run(main())
