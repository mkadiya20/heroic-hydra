from submission import Submission

class User:
    """User class containing information on user"""


    def __init__(self, username, socket) -> None:
        """Initialize with username"""

        # String that contains the error the user is targeting
        self.current_objective = ""
        self.username = username
        self.submission = None
        self.score = 0
        self.socket = socket

    def submit(self, submission_string):
        """Creats submission instance attached to the user"""

        self.submission = Submission(submission_string)

    def assign_objective(self, targetError):
        """Used by Game.py to assign a random error to a user"""

        self.current_objective = targetError
        self.socket.Send()

    def grade(self):
        """Adjusts score of user"""

        self.score += self.submission.hit_target(self.current_objective)
