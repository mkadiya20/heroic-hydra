import asyncio
import sys

import websockets


async def main():
    """Main async function."""
    async with websockets.connect("ws://localhost:8000") as socket:
        await socket.send(input("Username: "))
        while True:
            dat = await socket.recv()
            print(dat)
            code = input(
                "Enter code or (--leaderboard to see players, --exit to exit): "
            )
            if code == "--close":
                await socket.close()
                sys.exit()
            await socket.send(code)
            dat = await socket.recv()
            print(dat)


asyncio.run(main())
