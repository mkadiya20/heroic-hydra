#!/usr/bin/env python

import asyncio
import json
import tkinter as tk
from threading import Lock, Thread
from tkinter import Tk, ttk

import websockets

lock = Lock()
data = {
    "websocket": None,
    "objective": None,
    "score": 0,
    "submission": None,
    "leaderboard": None,
}


def get_objective():
    """Get the user data."""
    global data
    with lock:
        return data["objective"]


def get_leaderboard():
    """Get the leaderboard."""
    global data
    with lock:
        return data["leaderboard"]


def get_websocket():
    """Get the websocket."""
    with lock:
        return data["websocket"]


async def hello():
    global data
    async with websockets.connect("ws://localhost:8000") as websocket:
        with lock:
            data["websocket"] = websocket

        registration = {
            "user": f"{username}",
            "type": "register",
            "data": f"{username}",
        }

        await websocket.send(json.dumps(registration))

        while True:
            result = await websocket.recv()

            result = json.loads(result)

            if result["type"] == "login":
                print(result["data"])
            if result["type"] == "objective":
                with lock:
                    data["objective"] = result["data"]
            if result["type"] == "leaderboard":
                # print(result["data"])
                with lock:
                    data["leaderboard"] = result["data"]


def run():
    asyncio.run(hello())


async def write(websocket):
    """Send a message to the server."""
    with lock:
        submission = data["submission"]
        await websocket.send(json.dumps(submission))


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x600")
        self.root.title("Client")

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=3)
        self.root.rowconfigure(0, weight=1)

        self.editor_frame = ttk.Frame(self.root, padding=10)
        self.editor_frame.grid(row=0, column=0, sticky="nsew")

        self.info_frame = ttk.Frame(self.root, padding=10)
        self.info_frame.grid(row=0, column=1, sticky="nsew")

        self.text_editor = tk.Text(self.editor_frame)
        self.text_editor.insert(tk.END, "Hello World!")
        self.text_editor.pack(fill=tk.BOTH, expand=True)

        self.leaderboard = tk.Text(self.info_frame)
        self.leaderboard.insert(tk.END, "Leaderboard:")
        self.leaderboard.pack(fill=tk.BOTH, expand=True)

        self.current_objective = tk.Text(self.info_frame)
        self.current_objective.insert(tk.END, "Current Objective:")
        self.current_objective.pack(fill=tk.BOTH, expand=True)

        self.submit_button = ttk.Button(
            self.editor_frame, text="Submit Code", command=self.submit
        )
        self.submit_button.pack()

        self.root.after(0, self.update_leaderboard)
        self.root.after(0, self.update_current_objective)

        self.root.mainloop()

    def submit(self):
        """Pass the code to the server for submission"""
        print("Submitting code...")
        websocket = get_websocket()
        if websocket is None:
            print("No websocket")
            return
        code = self.text_editor.get("1.0", tk.END)
        submission = {
            "user": f"{username}",
            "type": "submit",
            "data": f"{code}",
        }
        with lock:
            data["submission"] = submission

        loop = asyncio.get_event_loop()
        loop.run_until_complete(write(websocket))

    def update_leaderboard(self):
        """Update the leaderboard with the given list"""
        leaderboard = get_leaderboard()
        self.leaderboard.delete(1.0, tk.END)

        if leaderboard is None:
            leaderboard = "Loading..."
            self.leaderboard.insert(tk.END, leaderboard)
        else:
            for key, value in leaderboard.items():
                self.leaderboard.insert(tk.END, f"{key}: {value}\n")

        self.root.after(1000, self.update_leaderboard)

    def update_current_objective(self):
        """Update the current objective with the given string"""
        objective = get_objective()
        if objective is None:
            objective = "Loading..."
        self.current_objective.delete(1.0, tk.END)
        self.current_objective.insert(tk.END, objective)
        self.root.after(1000, self.update_current_objective)


if __name__ == "__main__":
    from login_gui import Login_GUI

    login_gui = Login_GUI()
    username = login_gui.get_username()
    print(username)

    t = Thread(target=run)
    t.start()

    gui = GUI()
    t.join()
