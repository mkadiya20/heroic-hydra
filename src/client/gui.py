import tkinter as tk
from tkinter import Tk, ttk


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
        pass

    def update_leaderboard(self):
        """Update the leaderboard with the given list"""
        # data = client.get_data()
        # leaderboard = data["leaderboard"]
        leaderboard = "new leaderboard"
        self.leaderboard.delete(1.0, tk.END)
        self.leaderboard.insert(tk.END, leaderboard)
        self.root.after(1000, self.update_leaderboard)

    def update_current_objective(self):
        """Update the current objective with the given string"""
        # import client
        # data = get_data()
        # objective = data["objective"]
        objective = "new objective"
        self.current_objective.delete(1.0, tk.END)
        self.current_objective.insert(tk.END, objective)
        self.root.after(1000, self.update_current_objective)


# if __name__ == "__main__":
#     gui = GUI()
#     gui.update_current_objective("This is the new objective!")
