import tkinter as tk
from tkinter import Tk, ttk


class GUI:
    def __init__(self, root: Tk):
        root.geometry("800x600")
        root.title("Client")

        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=3)
        root.rowconfigure(0, weight=1)

        self.editor_frame = ttk.Frame(root, padding=10)
        self.editor_frame.grid(row=0, column=0, sticky="nsew")

        self.info_frame = ttk.Frame(root, padding=10)
        self.info_frame.grid(row=0, column=1, sticky="nsew")

        self.text_editor = tk.Text(self.editor_frame)
        self.text_editor.insert(tk.END, "Hello World!")
        self.text_editor.pack(fill=tk.BOTH, expand=True)

        self.leaderboard = tk.Text(self.info_frame)
        self.leaderboard.insert(tk.END, "Leaderboard:")
        self.leaderboard.config(state="disabled")
        self.leaderboard.pack(fill=tk.BOTH, expand=True)

        self.current_objective = tk.Text(self.info_frame)
        self.current_objective.insert(tk.END, "Current Objective:")
        self.current_objective.config(state="disabled")
        self.current_objective.pack(fill=tk.BOTH, expand=True)

        self.submit_button = ttk.Button(
            self.editor_frame, text="Submit Code", command=self.submit
        )
        self.submit_button.pack()

        root.mainloop()

    def submit(self):
        """Pass the code to the server for submission"""
        pass

    def update_leaderboard(self, leaderboard: list):
        """Update the leaderboard with the given list"""
        pass

    def update_current_objective(self, objective: str):
        """Update the current objective with the given string"""
        self.current_objective.delete(1.0, "END")
        self.current_objective.insert(tk.END, objective)


if __name__ == "__main__":
    gui = GUI(Tk())
    gui.update_current_objective("This is the new objective!")
