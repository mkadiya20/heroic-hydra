import subprocess
import sys


class ErrorGenerator:
    async def evaluate(self, error: str, code: str):
        """Checks if the code provided"""
        if "raise" in code:
            return -69000000, False  # Nice
        else:
            out = subprocess.run(
                f"{sys.executable} -c {code}",
                executable=sys.executable,
                timeout=10,
                capture_output=True,
                text=True,
            )
            if out.returncode == 0:
                return -1, False
            elif error in out.stderr:
                return 1, True
            else:
                return 0, False
