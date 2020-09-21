from Util import suffix

def t_suffix():

    for i in range(1, 31+1):
        print(str(i) + suffix(i))

def t_divmod():

    for i in range(1, 31+1):
        tens, units = divmod(i, 10)
        print("{} = {}{}".format(i, tens, units))

if __name__ == "__main__":
    t_suffix()
