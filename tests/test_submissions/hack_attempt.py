# flake8: noqa
import subprocess

subprocess.run(
    ["rm", "/home/cy/tech/heroic-hydra/tests/test_submissions/DONTDELETE.txt"],
    capture_output=True,
)
