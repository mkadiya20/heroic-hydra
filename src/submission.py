import sys
import os
import subprocess

class Submission:
    def __init__(self, file_path) -> None:
        self.file_path = file_path


    def get_error(self):
        """
        Runs the submission file and returns number of points it should earn
        """

        if self.check_cheating():
            return 0

        completed_process = subprocess.run(['python', self.file_path], 
                                            capture_output=True)
        error = completed_process.stderr
        
        return str(error)


    def hit_target(self, targetError):
        """
        Checks if the submission causes the target error
        """

        error = self.get_error()

        if not error: return False

        return targetError in error

    def check_cheating(self) -> bool:
        """
        Checks whether a submission contains 'raise' (and maybe check security)
        """
        pass


    def delete_submission(self):
        """
        Gets rid of the submission after it has been checked
        """
        pass

if __name__ == '__main__':
    # Run submission.py with name of a submission file for manual testing
    if len(sys.argv) == 3:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_name = sys.argv[1]
        full_path = dir_path + "/test_submissions/" + file_name
        
        targetError = sys.argv[2]
        sub = Submission(full_path)
        print(sub.hit_target(targetError))
    else:
        print("Arguments: submission filename, targetError")