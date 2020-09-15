from datetime import datetime
from sys import stderr

def input_() -> str:
    """
    Use this to input commands for Jarvis if the desired way fails
    """

    return input("Command: ")

def output(response: str):
    """
    Use this to output Jarvis's response if the desired way fails
    """

    print(response)

def log(msg: str):
    print("{} [Error] {}".format(datetime.now(), msg), file=stderr)
