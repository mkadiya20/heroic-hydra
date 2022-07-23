import os
import subprocess
import sys


class Submission:
    """Submission class"""

    def __init__(self, code_string) -> None:
        """Submission class initialized with full path to submission"""
        self.code_string = code_string

    def get_error(self):
        """Runs the submission file and returns the error that results"""

        res = subprocess.run(
            f"{sys.executable} -c {self.code_string}",
            executable=sys.executable,
            capture_output=True,
            text=True,
            timeout=10,
        )

        if int(res.returncode) == 0:
            return 0
        return res.stderr

    def hit_target(self, targetError):
        """Checks how many points the user should get"""
        if self.check_cheating():
            return -69

        out = self.get_error()

        if out.returncode == 0:
            return -1, False  # -1 point for no error?
        elif targetError in str(out.stderr):
            return 1, True
        else:
            return 0, False

    def check_cheating(self) -> bool:
        """Checks whether a submission contains 'raise' (and maybe check security)"""
        return "raise" in self.code_string


if __name__ == "__main__":
    # Run submission.py with name of a submission file for manual testing
    if len(sys.argv) == 3:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = sys.argv[1]
        full_path = dir_path + "/test_submissions/" + file_name
        text_file = open(full_path)
        code = text_file.read()
        targetError = sys.argv[2]
        sub = Submission(code)
        print(sub.hit_target(targetError))
    else:
        print("Arguments: submission filename, targetError")
