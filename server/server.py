from fastapi import FastAPI, WebSocket


app = FastAPI()


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    """This function is called when a websocket is opened."""
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")
