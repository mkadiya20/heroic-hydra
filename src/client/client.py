#!/usr/bin/env python

import asyncio
import json
from threading import Lock, Thread

import websockets

lock = Lock()


data = {"objective": None, "score": 0, "submission": None, "leaderboard": None}


def get_data():
    with lock:
        return data


# def get_objective():
#     with lock:
#         return data["objective"]


# def get_score():
#     with lock:
#         return data["score"]


# def get_submission():
#     with lock:
#         return data["submission"]


# def get_leaderboard():
#     with lock:
#         return data["leaderboard"]


async def hello():
    global data
    async with websockets.connect("ws://localhost:8000") as websocket:
        registration = {
            "type": "register",
            "data": username,
        }
        await websocket.send(json.dumps(registration))

        while True:
            result = json.loads(await websocket.recv())

            if result["type"] == "login":
                print(result["data"])
            if result["type"] == "objective":
                with lock:
                    data["objective"] = result["data"]
            if result["type"] == "leaderboard":
                lock.acquire()
                data["leaderboard"] = result["data"]
                lock.release()


def run():
    asyncio.run(hello())


if __name__ == "__main__":
    from gui import GUI
    from login_gui import Login_GUI

    login_gui = Login_GUI()
    username = login_gui.get_username()
    print(username)

    t = Thread(target=run)
    t.start()
    # t.join()

    gui = GUI()
    t.join()
    # gui.update_current_objective("New objective")
