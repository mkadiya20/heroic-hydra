to create a new user:
game.login(username)

to remove a user:
game.logout(username)

to give the user a new targetError:
game.newTarget(username)

to submit a string for evaluation and update users score:
game.submit(username, submission_string)

to return a single users score
game.user_score(username)

to return the full leaderboard
game.get_leaderboard()
