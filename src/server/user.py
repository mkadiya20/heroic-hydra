from submission import Submission


class User:
    """User class containing information on user"""

    def __init__(self, username) -> None:
        """Initialize with username"""

        # String that contains the error the user is targeting
        self.current_objective = ""
        self.username = username
        self.submission = None
        self.score = 0

    async def submit(self, submission_string):
        """Creates submission instance attached to the user"""

        self.submission = Submission(submission_string)
        return (await self.grade())

    async def assign_objective(self, targetError):
        """Used by Game.py to assign a random error to a user"""

        self.current_objective = targetError

    async def grade(self):
        """Adjusts score of user"""

        result = await self.submission.hit_target(self.current_objective)
        self.score += result[0]
        return result[1]
