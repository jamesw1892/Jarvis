from Util import suffix
import logging
import os

def t_suffix():

    for i in range(-31, 1):
        print(str(i) + suffix(i))

def t_divmod():

    for i in range(1, 31+1):
        tens, units = divmod(i, 10)
        print("{} = {}{}".format(i, tens, units))

def logging_exception():

    def f():
        try:
            raise Exception("Message in exception")
        except Exception as e:
            # this is the way to log an exception properly,
            # don't use kwarg stack_info
            logging.error("Message in log", exc_info=e)

    f()

def temp_loc():

    print(os.path.expandvars("%TEMP%"))

if __name__ == "__main__":
    temp_loc()
