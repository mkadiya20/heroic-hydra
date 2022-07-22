class ErrorGenerator:
    async def evaluate(self, error: str, code: str):
        """Checks if the code provided"""
        if "raise" in code:
            return -69000000, False  # Nice
        else:
            try:
                exec(code)
            except Exception as eval_error:
                if error in str(type(eval_error)):
                    return 1, True
                else:
                    return 0, False
            if "eval_error" not in locals():
                return -1, False
