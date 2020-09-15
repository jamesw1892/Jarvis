from Validation import true_false

class Speaker():
    """
    Class to allow Jarvis to speak to the user.
    """

    def __init__(self, AndroidSpeaker):

        self.droid = AndroidSpeaker()
    
    def speak(self, msg):
        """
        Function to allow Jarvis to speak to the user.
        ~
        PARAMETERS:
        - msg (string): The text for Jarvis to speak.
        ~
        RETURN:
        - error (boolean): Whether or not there is an error.
        - message (string): The error message if there is an error, otherwise, 'None'
        """

        try:
            out = self.droid.ttsSpeak(msg)
        except Exception as message:
            message = message
            error = True
        else:
            message = None
            if str(out).replace("Result(", "").replace(")","").split("error=")[-1] == "None":
                error = False
            else:
                error = True
        
        return(error, message)
    
    def remove_files(self):
        """
        Empty procedure to remove errors if not on windows.
        """

        return True

class Listener():
    """
    Class to listen for input from the user in windows 10.
    ~
    PARAMETERS:
    - AndroidListener (class): The class imported from 'androidhelper' library.
    """

    def __init__(self, AndroidListener):

        self.listener = AndroidListener()
    
    def listen(self):
        """
        Function to try to get input from the microphone.
        ~
        RETURNS:
        - error (boolean): Whether or not there is an error.
        - out (string): If 'error' = False, the text the user spoke into the microphone, if 'error' = True, "Error!".
        """

        try:
            out = self.listener.recognizeSpeech("Command: ", None, None)[1]
        except:
            error = True
            out = "Error!"
        else:
            error = False

        return(error, out)

def init_Jarvis_android(speak, listen):
    """
    Procedure to initialise Jarvis for android.
    ~
    PARAMETERS:
    - speak (boolean): Whether or not Jarvis will speak back.
    - listen (boolean): Whether or not Jarvis will listen to you speak.
    """

    from Jarvis import main

    if speak:
        try:
            from androidhelper import Android as AndroidSpeaker
        except:
        	    from android import Android as AndroidSpeaker

        speaker = Speaker(AndroidSpeaker)
    else:
        speaker = None
    
    if listen:
        from androidhelper.sl4a import Android as AndroidListener

        listener = Listener(AndroidListener)
    else:
        listener = None
    
    main("android", speak, listen, speaker, listener)

if __name__ == "__main__":

    speak = true_false("Would you like me to Speak? ")
    listen = true_false("Would you like me to listen? ")

    init_Jarvis_android(speak, listen)