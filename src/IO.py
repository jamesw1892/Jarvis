from datetime import datetime
import logging

handler_file = logging.FileHandler("jarvis.log")
handler_file.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s", "%Y-%m-%d %H:%M:%S"))

handler_stderr = logging.StreamHandler()
handler_stderr.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler_file,
        handler_stderr
    ]
)

def stdin() -> str:
    """
    Use this to input commands for Jarvis if the desired way fails
    """

    return input("Command: ")

def stdout(response: str):
    """
    Use this to output Jarvis's response if the desired way fails
    """

    print(response)
