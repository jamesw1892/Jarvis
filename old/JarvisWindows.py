from Validation import true_false
from os import system

class Speaker():
    """
    Class to store a count variable and remove all the files created after they have been spoken.
    ~
    PARAMETERS:
    - allowed_dir (string): The allowed directory to save files too to play.
    """

    def __init__(self, allowed_dir, system, remove, gTTS):

        self.count = 0
        self.dir = allowed_dir
        self.history = {}
        self.system = system
        self.remove = remove
        self.gTTS = gTTS
    
    def speak(self, msg):
        """
        Function to speak a msg while remembering all previous speeches.
        ~
        PERAMETERS:
        - msg (string): Message to speak.
        ~
        RETURNS:
        - error (boolean): Whether or not there is an error.
        - message (string): The error message if there is an error, otherwise, 'None'
        """

        message = None

        if msg in self.history:
            self.system(self.dir + str(self.history[msg]) + ".mp3")
            error = False
        else:
            try:
                tts = self.gTTS(msg)
                tts.save(self.dir + str(self.count) + ".mp3")
            except Exception as e:
                message = str(e)
                error = True
            else:
                error = False
                self.history[msg] = self.count
                self.system(self.dir + str(self.count) + ".mp3")
                self.count += 1
        
        return(error, message)
        
    def remove_files(self):
        """
        Procedure to remove all audio files once done.
        """
        
        system("TASKKILL /F /IM wmplayer.exe")
        for count in range(self.count):
            self.remove(self.dir + str(count) + ".mp3")

class Listener():
    """
    Class to listen for input in windows 10.
    ~
    PARAMETERS:
    - sr (class): The class imported from the 'speech_recognition' library.
    """

    def __init__(self,sr):

        self.sr = sr
        self.listener = sr.Recognizer()
    
    def listen(self):
        """
        Function to try to get input from the microphone.
        ~
        RETURNS:
        - error (boolean):  Whether or not there is an error.
        - out (string): If 'error' = False, the text the user spoke into the microphone, if 'error' = True, the error message.
        """

        with self.sr.Microphone() as source:
            self.listener.adjust_for_ambient_noise(source)
            print("Command: ")
            audio = self.listener.listen(source)
            
        try:
            out = self.listener.recognize_google(audio) #must be online for this
        except self.sr.UnknownValueError:
            error = True
            out = "Could not understand audio"
        except self.sr.RequestError as e:
            error = True
            out = "Could not request results; " + str(e)
        else:
            error = False
        return(error, out)

def init_Jarvis_win10(speak, listen, allowed_dir="./"):
    """
    Procedure to initialise Jarvis for windows 10.
    ~
    PARAMETERS:
    - speak (boolean): Whether or not Jarvis will speak back.
    - listen (boolean): Whether or not Jarvis will listen to you speak.
    - allowed_dir (string): The allowed directory to save audio files. Default="./" (current directory).
    """

    from Jarvis import main

    if speak:
        from os import system, remove
        from gtts import gTTS

        speaker = Speaker(allowed_dir, system, remove, gTTS)
    else:
        speaker = None
    
    if listen:
        import speech_recognition as sr

        listener = Listener(sr)
    else:
        listener = None
    
    main("win10", speak, listen, speaker, listener)

if __name__ == "__main__":

    speak = true_false("Would you like me to Speak? ")
    listen = true_false("Would you like me to listen? ")
    if speak:
        allowed_dir = input("Allowed Directory (blank for default): ")
        if allowed_dir == "":
            allowed_dir = "C:/Users/defaultuser0/Music/"
    else:
        allowed_dir = "C:/Users/defaultuser0/Music/"

    init_Jarvis_win10(speak, listen, allowed_dir)