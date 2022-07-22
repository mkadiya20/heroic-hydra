from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/")
async def root(websocket: WebSocket):
    """This function is called when a websocket connection is made to http://localhost:8000/ (root of the api)."""
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")