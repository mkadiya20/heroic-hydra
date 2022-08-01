# SNEKBOX SANDBOX
[Snekbox](https://github.com/python-discord/snekbox) provides a safe way to run user submitted code with some extra setup. This is enabled by default in security_config.py.
If you trust all the users and just want to execute the code directly on the server, change `SNEKBOX_ENABLE` to False in security_config.py.
Otherwise, the following steps must be taken to setup snekbox on the server.

- [Install docker on server and start it](https://docs.docker.com/desktop/)
- Download and run the snekbox image from the GitHub conatiner registry with CLI:
`docker run --ipc=none --privileged -p 8060:8060 ghcr.io/python-discord/snekbox`

## Many Players

The default snekbox image installed above includes 2 workers for parallel execution of code. If significantly more users are expected, then a custom snekbox image may have to be built with a change to the default number of workers so that code execution from one user doesn't block another.

Instructions for how to do this are in the [snekbox repo](https://github.com/python-discord/snekbox)
