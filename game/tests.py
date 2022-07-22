import asyncio
import json

import aiohttp
import websockets


async def request(session, url):
    async with session.get(url) as sesh:
        return await sesh.json()


URL = "localhost:8000"


class Client:
    def __init__(self):
        self.ws = None
        self.nonce = 0

    async def login(self) -> None:
        """Logs in."""
        self.ws = await websockets.connect(f"ws://{URL}")

    async def receive(self) -> str:
        return await self.ws.recv()

    async def _request(self, request: dict) -> None:
        """Sends a request and returns the response."""
        self.nonce += 1
        await self.ws.send(json.dumps(request))

    async def ping(self) -> str:
        """Pings API."""
        return await self._request({"message": "ping"})


client = Client()


async def main():
    """Just a test client."""
    session = aiohttp.ClientSession()
    await client.login()
    print(await client.receive())
    while True:
        user_input = input("Enter Username: ")
        await client._request(user_input)
        if await client.receive() != "ERROR":
            break
    try:
        while True:
            print(await client.receive())
            while True:
                user_input = input(
                    "Enter something: (Enter --leaderboard to see the leaderboard)"
                )
                if user_input == "--leaderboard":
                    print(await request(session, "http://localhost:8000/leaderboard"))
                else:
                    await client._request(user_input)
                    print(await client.receive())
                    break
    except KeyboardInterrupt:
        await session.close()
        client.ws.close()


asyncio.run(main())
