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

The JSON structure of responses from the server will be `{"type": "error" or "text", "error" or "text": str}`

i.e
`{"type": "error", "error": "You must register first"}`
`{"type": "text", "text": "Your code raised the correct error!"}`

Responses with type "error" automatically close the websocket after sending, while type "text" do not, and only send text.



The server expects JSON requests with the structure:
`{"type": "leaderboard" or "logout" or "register" or "test" or "submission", ("data": str) or None}`

Sending a type "leaderboard" request (takes no data), sends back a type "text" with the leaderboard (as string).

Sending a type "logout" request (takes no data) sends back no response.

Sending a type "register" request (Takes a username as data), sends back a type "text" or "error" with the error or text associated with registering.

Sending a type "test" request (takes code as data), sends back a type "text" with the whether or not the code provided raised error specified.

NOTE: A type "test" request, does not change the user's points, it just returns whether or not the code raised the error specified.

Sending a type "submission" request, sends back a type "text" with the whether or not the code raised the error specified.

i.e
`{"type": "leaderboard"} (returns a string of the leaderboard)`
`{"type": "register", "data": "HRLO77"} (logs user in)`
`{"type": "test", "data": "print('hello world!')"} (sends code "print('hello world')" to test if it raises the error intended)`


Order of requests and responnses for building a client:

    1. Server sends "register" type request.

    2. Client recieves response of registration. (type either "text" or "error").

    3. Server sends type "text" response (error that must be produced).

    4. Client sends request (can be of any type specified).

    5. Server sends response of any type "error" or "text".

Steps 3, 4 and 5 (in consecutive order) are repeated after steps 1 and 2, until websocket is closed.
