[GitHub URL]: https://github.com/mkadiya20/heroic-hydra.git
[Python]: https://www.python.org/downloads/release/python-3100/
[Project Dependencies]: https://github.com/mkadiya20/heroic-hydra/blob/67f188d0a955d1ae60e08e426ccc68b27ff27e15/poetry.lock
[Docker URL]: https://docs.docker.com/desktop/
# <font color="#FF4040"> Error </font> Race

---
> <img src = "https://i1.theportalwiki.net/img/thumb/9/92/Bendy.png/120px-Bendy.png" width="30"> <font size="100"> Hello</font> <code> <u> f"{self.reader.nickname}</u> !"</code>
> <br> Welcome to <font color="#FF4040"> Error </font> Race!   The game that believes that bugs should be features.. <s>even if they are actually bugs</s> Always!!
> <br> <br> <br> <br> 
> <img src="https://www.pythondiscord.com/static/images/events/summer_code_jam_2022/site_banner.png">

> ### Requirements:
> - [Dependencies][Project Dependencies]
> - [Python 3.10][Python]
> - [GitHub Repository][GitHub URl]
> - [Docker][Docker URl]

> ### Setup
> #### Install Dependencies
> You can install the required libraries using the following command:
>  > ```commandline
>  > poetry install
> > ```
>
> #### Tkinter Install
> If you do not have Tkinter installed with your current python build, then follow the steps outlined [here](https://tkdocs.com/tutorial/install.html)
> #### Snekbox setup
> Security is important, so this project comes with [Snekbox](https://github.com/python-discord/snekbox)! You can turn this off if you wish via the [security config](https://github.com/mkadiya20/heroic-hydra/blob/fbeeb8492af96d7b26aa74c5e22a1fc564a5f4e4/src/server/security_config.py) file.
> > Setup & Initialize Snekbox with the following command:
> > ```commandline
> > docker run --ipc=none --privileged -p 8060:8060 ghcr.io/python-discord/snekbox
> > ```
> #### Starting the Server
> Starting the server is simple. Navigate to ``.../src/server`` with the following command: 
> > ```cd src/server``` | ```cd ...src/server```
> 
> Then run the following command:
> > ```commandline
> > python -m uvicorn server:app --reload --timeout-keep-alive 9999999999999 --ws websockets --ws-max-size 1024 --loop asyncio
> > ```
> #### Starting the Client
> Starting the client is just about the same as starting the server. 
> > Utilizing another Terminal window: navigate to ``...src/client`` with the following command:
> > > ```cd src/client``` | ```cd ...src/client```
>
> Then run the following:
> > ```commandline
> > python client.py
> > ```
> #### Playing the game
> Playing the game is as simple as 1 2 3 except minus the 3. 
> > First, login with a username of your choice.\
> > Second, attempt to replicate the error objective given to you. When you've reproduced the error xor think you have. Click the Submit button.
> <center> <font size="044"> Don't Cheat </font> <center> </center> 
> <center> <img src="https://i1.theportalwiki.net/img/thumb/9/9d/AngerCore.png/250px-AngerCore.png" width="70"> </center> </center>
