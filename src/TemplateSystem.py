import Core
import IO
import logging

# Put any medium-specific imports in the methods (not here) so that if a user
# does not have a library, they can avoid errors by not selecting that
# medium so it is never tried to be imported. See Windows.py for an example

class Inputter:
    """
    Manage getting commands from the user on this system in the preferred
    way if possible
    """

    def __init__(self, medium):
        """Instantiate the inputter, providing the preferred medium to use"""

        self.medium = medium

    def input_(self) -> str:
        """Input a command from the user using the preferred medium if possible"""

        # Try to input through the prefered medium, but revert to
        # backup if need to and log any errors found, for example:
        # logging.error("Problem!")

        return IO.stdin()

class Outputter:
    """
    Manage outputting the response from Jarvis on this system in the preferred
    way if possible
    """

    def __init__(self, medium):
        """Instantiate the outputter, providing the preferred medium to use"""

        self.medium = medium

    def output(self, response: str):
        """Output the given response to the preferred medium if possible"""

        # Try to output through the prefered medium, but revert to
        # backup if need to and log any errors found, for example:
        # logging.error("Problem!")

        IO.stdout(response)

def main(input_medium, output_medium):
    """
    Run Jarvis on this system using the given
    preferred input and output media if possible
    """

    Core.main(Inputter(input_medium), Outputter(output_medium))

if __name__ == "__main__":
    main(True, True)
