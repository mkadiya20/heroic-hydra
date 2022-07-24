# Game.py

to create a new user:
game.login(username)

to remove a user:
game.logout(username)

to give the user a new targetError:
game.newTarget(username, error)

to submit a string for evaluation and update users score:
game.submit(username, submission_string)

to return a single users score
game.user_score(username)

to return the full leaderboard
game.get_leaderboard()

# Server.py

Connect to the server by connecting to ws://localhost:8000/.

When you first connect, it will expect for a JSON response (for logging in). (Remember, when sending JSON you must do
`json.dumps(dictionary)`)

Afterward, it will continously send a random error for the client to reproduce, followed by a response. (JSON structure response is explained further.)

The JSON structure of responses from the server will be `{"type": "error" or "leaderboard" or "objective" or "test" or "submit" or "login", "data": str or dict}`

i.e
`{"type": "error", "data": "You must register first"}`
`{"type": "leaderboard", "data": {"HRLO77": 13, "Barko": 7, "mkadiya": 3}} (NOTE: when getting type "leaderboard" responses, the dict is ordered from greatest to least, left to right.)`
`{"type": "objective": "data": "Produce error SyntaxError"}`
`{"type": "submit": "data": "Your code did not raise the error specified."}`

Responses with type "error" automatically close the websocket after sending, while the other types do not.

The server expects JSON requests with the structure:
`{"type": "leaderboard" or "logout" or "register" or "test" or "submit", ("data": str) or None}`

Sending a type "leaderboard" request (takes no data), sends back a type "leaderboard" with the leaderboard (dict as specified before).

Sending a type "logout" request (takes no data) sends back no response.

Sending a type "register" request (Takes a username as data), sends back a type "login" or "error" with the error or text associated with registering.

Sending a type "test" request (takes code as data), sends back a type "test" with the whether or not the code provided raised error specified.

NOTE: A type "test" request, does not change the user's points, it just returns whether or not the code raised the error specified.

Sending a type "submit" request, sends back a type "submit" with the whether or not the code raised the error specified.

Closing the websocket makes the server logout the user from the game and clean up the connection (so does request type "logout").

i.e
`{"type": "leaderboard"} (returns a dict of the leaderboard)`
`{"type": "register", "data": "HRLO77"} (logs user in)`
`{"type": "test", "data": "print('hello world!')"} (sends code "print('hello world')" to test if it raises the error intended)`


Order of requests and responnses for building a client:

    1. Server sends "register" type request.

    2. Client recieves response of registration. (type either "login" or "error").

    3. Server sends type "objective" response (error that must be produced).

    4. Client sends request (can be of any type specified).

    5. Server sends response of any type.

Steps 3, 4 and 5 (in consecutive order) are repeated after steps 1 and 2, until websocket is closed.
