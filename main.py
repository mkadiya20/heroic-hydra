import asyncio
import uvicorn
from Client import client


async def start():
    c = client.Client()

    await c.login()
    print(await c.ping())


# Currently only runs the first of the 2 lines
asyncio.run(start())
uvicorn.run("server:app", port=8080, app_dir="./server", loop="asyncio")
