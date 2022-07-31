import asyncio

from uvicorn import Config, Server

from Client import client
from server.server import app


async def start():
    c = client.Client()

    await c.login()
    print(await c.ping())


loop = asyncio.new_event_loop()
config = Config(app=app, loop=loop, port=8080)
server = Server(config)
loop.create_task(server.serve())
loop.create_task(start())
# uvicorn.run("server:app", port=8080, app_dir="./server", loop="asyncio")
loop.run_forever()
