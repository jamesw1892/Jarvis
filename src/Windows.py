from BackupIO import input_, output, log
from typing import Union
from os import system, remove

class WindowsInputter:
    def __init__(self, to_listen: bool):
        self.to_listen = to_listen
        if self.to_listen:
            try:
                import speech_recognition as sr
                self.sr = sr
                self.listener = sr.Recognizer()
            except ImportError:
                log("Could not input listener")
                self.to_listen = False

    def listen(self) -> Union[bool, str]:

        with self.sr.Microphone() as source:
            self.listener.adjust_for_ambient_noise(source)
            output("Speak now")
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
                log(cmd_or_error_msg)
            else:
                return cmd_or_error_msg

        return input_()

class WindowsOutputter:
    def __init__(self, to_speak: bool):
        try:
            from gtts import gTTS
        except ImportError:
            log("Could not import gtts for WindowsOutputter to speak")

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
                message = str(e)
                error = True

        return error, message

    def output(self, response: str):

        if self.to_speak:
            is_error, error_msg = self.speak(response)
            if is_error:
                log(error_msg)
                output(response)
        else:
            output(response)

def main(to_listen: bool, to_speak: bool):
    # TODO
    pass
