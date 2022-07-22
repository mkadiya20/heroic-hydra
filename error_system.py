import os

try:
    import keyboard
except ImportError:
    os.system("pip install keyboard")
    import keyboard


class ErrorGenerator:

    @staticmethod
    def __failure(reason: str, sub_reason: str = ""):
        print(
            f"You failed... \n Reason: \033[01m\033[31m{reason}\033[0m \n Sub-Reason: {sub_reason} \n Press ENTER to continue.")
        if keyboard.read_key() == "ENTER":
            return None

    @staticmethod
    def __passed(point_gain: int):
        print(
            f"You Passed!  \n Points Gained: \033[01m\033[32m{point_gain}\033[0m \n Press ENTER to continue.")
        if keyboard.read_key() == "ENTER":
            return None

    def evaluate(self, error: str, code: str):

        if code.__contains__("raise"):
            self.__failure("Cheating", "Please do not use raise, it's in the rules. :(")
            return -69_000_000, False
        else:
            try:
                eval(code)
            except Exception as eval_error:
                if error in str(type(eval_error)):
                    self.__passed(1)
                    return 1, True
                else:
                    self.__failure(f"Error is not {error}.")
                    return 0, False
            if 'eval_error' not in locals():
                self.__failure("No Errors", f"You need to produce {error}")
                return 0, False


def example():
    error_generator = ErrorGenerator()
    print(error_generator.evaluate("ValueError", "int(1)"))
