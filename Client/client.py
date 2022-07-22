import json

import websockets

URL = "localhost:8080"


class Client:
    def __init__(self):
        self.ws = None
        self.nonce = 0

    async def login(self) -> None:
        self.ws = await websockets.connect(f"ws://{URL}")

    async def _request(self, request: dict) -> str:
        self.nonce += 1
        await self.ws.send(json.dumps(request))
        return await self.ws.recv()

    async def ping(self) -> str:
        return await self._request({"message": "ping"})
