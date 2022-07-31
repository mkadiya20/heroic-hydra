from tkinter import StringVar, Tk, ttk


class Login_GUI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x150")
        self.root.title("Login")

        global username
        username = StringVar()

        self.user_label = ttk.Label(self.root, text="Username:").grid(row=0, column=0)
        self.user_entry = ttk.Entry(self.root, textvariable=username).grid(
            row=0, column=1
        )

        self.login_button = ttk.Button(
            self.root, text="Login", command=self.login
        ).grid(row=0, column=2)

        self.root.mainloop()

    def set_username(self, username: str):
        """Set the username for the client"""
        self.username = username

    def get_username(self) -> str:
        """Get the username for the client"""
        return self.username

    def login(self):
        """Login the client and close the window"""
        self.set_username(username.get())
        self.root.destroy()
