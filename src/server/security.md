# SNEKBOX SANDBOX
Snekbox provides a relatively safe way to run user submitted code with some extra setup.

- [Install docker on server and start it](https://docs.docker.com/desktop/)
- Download the snekbox image with CLI
`docker run --ipc=none --privileged -p 8060:8060 ghcr.io/python-discord/snekbox`


# User method

To prevent users from using submitted code to hack the server, a low-permission user can be created on the server machine
to execute the submitted code without permissions.

This project searches for a user called 'no_access' to assign to that role. If there is no user called 'no_access', then
the submitted code will just be executed as whatever user runs the server process.

In linux, create a no_access user with
`sudo useradd no_access`

If the server is run in a python virtual environment, then the 'no_access' user must have traversal (execute) permissions for each directory on the way to the python interpreter symbolic link in the virtual environment.

The 'no_access' should have execute permissions by default for the base interpreter by default, but if not, then that
must be changed as well.

To untilize this feature, the server must be started with superuser privileges and the path to the python virtual environment interpreter must be explicitly used when starting the server:

`sudo ../../.venv/bin/python -m uvicorn server:app --reload --timeout-keep-alive 9999999999999 --ws websockets --ws-max-size 1024 --loop asyncio`
