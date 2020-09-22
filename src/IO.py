from datetime import datetime
import logging

# LOGGING SETTINGS

# Save detailed information to log file
handler_file = logging.FileHandler("jarvis.log")
handler_file.setFormatter(logging.Formatter(
    "%(asctime)s %(levelname)s %(filename)s:%(lineno)d - %(message)s",
    "%Y-%m-%d %H:%M:%S"
))

# Output simple information to stderr
handler_stderr = logging.StreamHandler()
handler_stderr.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

# Log everything of level INFO or higher (everything apart from DEBUG)
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler_file,
        handler_stderr
    ]
)

# END LOGGING SETTINGS

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
