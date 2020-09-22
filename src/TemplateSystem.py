import Core
import IO
import logging

class Inputter:
    def __init__(self, medium):
        self.medium = medium

    def input_(self) -> str:

        # Try to input through the prefered medium, but revert to
        # backup if need to and log any errors found, for example:
        # logging.error("Problem!")

        return IO.stdin()

class Outputter:
    def __init__(self, medium):
        self.medium = medium

    def output(self, response: str):

        # Try to output through the prefered medium, but revert to
        # backup if need to and log any errors found, for example:
        # logging.error("Problem!")

        IO.stdout(response)

def main(input_medium, output_medium):
    Core.main(Inputter(input_medium), Outputter(output_medium))

if __name__ == "__main__":
    main(True, True)
