from error_thrower import Error_Objective
from submission import Submission

error_obj = Error_Objective()

MOD_THRESH = 5
HARD_THRESH = 10


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
        return await self.grade()

    async def assign_objective(self):
        """
        Used by Game.py to assign a error to a user with difficulty based
        on current score.
        """

        if self.score >= HARD_THRESH:
            difficulty = "HARD"
        elif self.score >= MOD_THRESH:
            difficulty = "MOD"
        else:
            difficulty = "EASY"

        self.current_objective = error_obj.objective(difficulty, 1)

        return self.current_objective

    async def grade(self):
        """
        Judges submission and adjusts users score accordingly.
        The results are also returned.
        """

        result = await self.submission.hit_target(self.current_objective)
        self.score += result[0]
        return result[1]
