import Core
import IO
import logging
import os
from typing import Union

class Inputter:
    """
    Manage getting commands from the user on Windows, listening to the user's
    voice if requested and possible
    """

    def __init__(self, to_listen: bool):
        """
        Instantiate the inputter.

        to_listen is a boolean indicating whether to listen to the user's
        voice if possible.
        """

        self.to_listen = to_listen
        if self.to_listen:

            # log import errors or initialise the listener
            try:
                import speech_recognition as sr
            except ImportError as e:
                logging.error("Could not import speech_recognition, reverting to standard input", exc_info=e)
                self.to_listen = False
            else:
                try:
                    import pyaudio
                except ImportError as e:
                    logging.error("Could not import pyaudio, reverting to standard input", exc_info=e)
                    self.to_listen = False
                else:
                    self.sr = sr
                    self.listener = sr.Recognizer()

    def listen(self) -> Union[str, None]:

        # listen
        with self.sr.Microphone() as source:
            self.listener.adjust_for_ambient_noise(source)
            IO.stdout("Listening...")
            audio = self.listener.listen(source)
            IO.stdout("Recognising...")

        cmd = None
        try:
            cmd = self.listener.recognize_google(audio, language="en-GB")
        except self.sr.UnknownValueError as e:
            logging.warning("Could not understand audio, try again")
            return self.listen()
        except self.sr.RequestError as e:
            # NOTE: default API key only allows 50 requests per day
            logging.error("Could not request results - no internet connection or invalid API key, temporarily reverting to standard input", exc_info=e)

        return cmd

    def input_(self) -> str:
        """
        Input a command from the user, listening to their voice if
        requested and possible
        """

        if self.to_listen:
            try:
                cmd = self.listen()

            # if there was an unknown error, log it and default to stdout this time
            except Exception as e:
                logging.error("Unknown error when listening, permanently reverting to standard input", exc_info=e)
                self.to_listen = False

            # if there was no error, return it
            else:
                if cmd is not None:
                    return cmd

                # if there was a known error, it has already been logged so use stdout temporarily

        return IO.stdin()

class Outputter:
    def __init__(self, to_speak: bool):
        self.to_speak = to_speak
        if to_speak:
            try:
                from gtts import gTTS
                from gtts.tts import gTTSError
            except ImportError as e:
                logging.error("Could not import speaker, reverting to standard output", exc_info=e)
                self.to_speak = False

        self.dir = "C:/Users/defaultuser0/Music/"
        self.count = 0
        self.history = dict()
        self.gTTS = gTTS
        self.gTTSError = gTTSError

    def speak(self, text: str) -> bool:

        errored = False

        # if already said it, run the existing file
        if text in self.history:
            os.system("{}{}.mp3".format(self.dir, self.history[text]))

        else:
            file_location = "{}{}.mp3".format(self.dir, self.count)
            audio = self.gTTS(text)
            try:
                audio.save(file_location)
            except PermissionError as e:
                logging.error("Don't have permission to save file, permanently reverting to standard output", exc_info=e)
                errored = True
            except self.gTTSError as e:
                logging.error("Error with API request, permanently reverting to standard output, inference of error: {}".format(e.infer_msg(audio)), exc_info=e)
                errored = True
                self.to_speak = False
            else:
                self.history[text] = self.count
                os.startfile(file_location)
                self.count += 1

        return errored

    def output(self, response: str):

        if self.to_speak:
            try:
                errored = self.speak(response)
            except Exception as e:
                logging.error("Unknown error when speaking, permanently reverting to standard output", exc_info=e)
                self.to_speak = False
            else:
                if not errored:
                    return

        IO.stdout(response)

def main(to_listen: bool, to_speak: bool):
    """
    Run Jarvis on Windows. to_listen is a bool representing
    whether to try listening to the user for input (otherwise
    will get input from standard input). to_speak is a bool
    representing whether to try speaking to the user (otherwise
    will print to standard output).
    """

    Core.main(Inputter(to_listen), Outputter(to_speak))

if __name__ == "__main__":
    main(True, True)
