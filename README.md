# Error Race - An Educational Game where the Goal is to Fail

Error Race is a game where players submit python code that tries to achieve an objective. The twist is that the objectives are different types of errors!

Test your knowledge of python execptions and play against multiple friends.

## Run the Game
*Instructions below assume that you have python and pip installed already.*

1. Clone this repository.

   `git clone https://github.com/mkadiya20/heroic-hydra.git`

2. (Optional) Setup virtual environment.
3. [Install tkinter](https://tkdocs.com/tutorial/install.html)
4. Install dependencies:

   `poetry install`

5. Setup snekbox on server for security or change `SNEKBOX_ENABLED` to `False` in security_config.py. To setup snekbox:
   - [Install docker on server and start it](https://docs.docker.com/desktop/)
   - Download, install, and run [docker](https://www.docker.com/products/docker-desktop/) for your version.
   - Download and run the snekbox image from the GitHub container registry with CLI:

      `docker run --ipc=none --privileged -p 8060:8060 ghcr.io/python-discord/snekbox`

6. Navigate to src/server and execute the following command to start the server:

   `python -m uvicorn server:app --reload --timeout-keep-alive 9999999999999 --ws websockets --ws-max-size 1024 --loop asyncio`

7. In another terminal, navigate to src/client and execute the following command to start a client.

   `python client.py`

## Play the Game
1. Login with username of your choosing.
2. Attempt to generate the error indicated in the bottom right textbox by writing code in the left box and hitting "Submit Code" button.

The leaderboard in the top right shows currently logged in players and their score.

Difficulty will ramp up as your score rises.

Leave the game by closing the GUI and the terminal.
