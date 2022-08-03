import os
import socket

os.system(f"echo {socket.gethostbyname(socket.gethostname())} is my ip address")
os.system(
    f"python -m uvicorn server:app --host {socket.gethostbyname(socket.gethostname())}"
)
