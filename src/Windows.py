import Core
import IO
import logging
from typing import Union
from os import system, remove

class Inputter:
    def __init__(self, to_listen: bool):
        self.to_listen = to_listen
        if self.to_listen:
            try:
                import speech_recognition as sr
                self.sr = sr
                self.listener = sr.Recognizer()
            except ImportError as e:
                logging.exception("Could not import listener", exc_info=e, stack_info=e.__traceback__)
                self.to_listen = False

    def listen(self) -> Union[bool, str]:

        with self.sr.Microphone() as source:
            self.listener.adjust_for_ambient_noise(source)
            IO.stdout("Speak now")
            audio = self.listener.listen(source)

        is_error = False
        try:
            cmd_or_error_msg = self.listener.recognize_google(audio) # NOTE: must be online
        except self.sr.UnknownValueError:
            is_error = True
            cmd_or_error_msg = "Could not understand audio"
        except self.sr.RequestError as e:
            is_error = True
            cmd_or_error_msg = "Could not request results; " + str(e)

        return is_error, cmd_or_error_msg

    def input_(self) -> str:
        if self.to_listen:
            is_error, cmd_or_error_msg = self.listen()
            if is_error:
                logging.error(cmd_or_error_msg)
            else:
                return cmd_or_error_msg

        return IO.stdin()

class WindowsOutputter:
    def __init__(self, to_speak: bool):
        try:
            from gtts import gTTS
        except ImportError as e:
            logging.exception("Could not import gtts for WindowsOutputter to speak", exc_info=e, stack_info=e.__traceback__)

        self.dir = "C:/Users/defaultuser0/Music/"
        self.to_speak = to_speak
        self.count = 0
        self.history = {}
        self.gTTS = gTTS

    def speak(self, msg: str):

        message = None
        error = False

        if msg in self.history:
            system(self.dir + str(self.history[msg]) + ".mp3")
        else:
            try:
                tts = self.gTTS(msg)
                tts.save(self.dir + str(self.count) + ".mp3")
                self.history[msg] = self.count
                system(self.dir + str(self.count) + ".mp3")
                self.count += 1
            except Exception as e:
                logging.exception("Could not speak", exc_info=e)
                message = str(e)
                error = True

        return error, message

    def output(self, response: str):

        if self.to_speak:
            is_error, error_msg = self.speak(response)
            if is_error:
                IO.stdout(response)
        else:
            IO.stdout(response)

def main(to_listen: bool, to_speak: bool):
    Core.main(Inputter(to_listen), WindowsOutputter(to_speak))

if __name__ == "__main__":
    main(True, True)
