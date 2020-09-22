from Validation import true_false
from random import choice
from DateTime import CurrentDateTime

def id_cmd(cmd):
    """
    Function to identify what the user has input and output what Jarvis needs to reply.
    ~
    PARAMETERS:
    - cmd (string): The command to process.
    ~
    RETURNS:
    - out (string): The output of Jarvis.
    """

    cmd = " " + cmd.lower() + " "
    allowed_chrs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "1","2","3","4","5","6","7","8","9","0"," "]
    temp = cmd
    cmd = ""
    for char in temp:
        if char in allowed_chrs:
            cmd += char
        else:
            cmd += " "

    if "say" in cmd:
        out = cmd.split("say")[1][1:-1]
    else:
        if "identify yourself" in cmd or (" what " in cmd and " name " in cmd) or (" are " in cmd and " you " in cmd and (" who " in cmd or " what " in cmd)):
            out = "My name is Jarvis"
        
        elif "who won the fa cup 1973" in cmd:
            out = "Sunderland A F C"
        
        elif " jarvis " in cmd:
            out = "Jarvis at your service"
        
        elif "are you ok" in cmd or "how are you" in cmd:
            out = "I'm great, thanks for asking"

        elif " password " in cmd:
            out = "I'll never tell you!"
            
        elif " who " in cmd and (" made " in cmd or " creat" in cmd):
            out = "jamesw1892"
            
        elif " hi " in cmd or " hello " in cmd or (" good " in cmd and (" morning " in cmd or " afternoon " in cmd or " evening " in cmd or " night " in cmd or " day " in cmd)):
            
            out = choice(["good", "hello", "hi"])
            if out == "good":
            
                i = CurrentDateTime()
                hours = int(i.get_hours())
                if hours < 12:
                    out = "Good morning"
                elif hours < 18:
                    out = "Good afternoon"
                else:
                    out = "Good evening"
            
        elif " time " in cmd and " what " in cmd:
            i = CurrentDateTime()
            out = "it is " + i.get_time_clock(12)
            
        elif " what" in cmd and (" day " in cmd or " date " in cmd or " year " in cmd or " month " in cmd):
            
            i = CurrentDateTime()
            out = "it is " + i.get_date_words()

        else:
            out = "I don't know what you mean by that"
    
    return(out)

def main(os, speak, listen, speaker=None, listener=None):
    """
    Procedure to manage Jarvis for any operating system.
    ~
    PARAMETERS:
    - os (string): The operating system - either 'win10' or 'android'.
    - speak (boolean): Whether or not to speak output.
    - listen (boolean): Whether or not to listen for input.
    - speaker (class instance): If speaking, the instance of the speaker class, if not speaking, None (default).
    - listener (class instance): If listening, the instance of the listener class, if not listening, None (default).
    """

    #test listening and speaking if turned on and if they don't work, revert to text-based.
    if speak:
        error, message = speaker.speak("Jarvis at your service")
        if error:
            print("Error when speaking, error:")
            print(message)
            print("Reverting to text-based input")
            speak = False
    
    if not speak:
        print("Jarvis at your service")
    
    if listen:
        again = true_false("Command? ")
        if again:
            error, cmd = listener.listen()
            if error:
                print("Error when listening, error:")
                print(cmd)
                print("Reverting to text-based input")
                listen = False
        else:
            cmd = ""
    
    if not listen:
        cmd = input("Command: ")

    error = False

    while cmd != "" and not error:
        if speak:
            error, cmd = speaker.speak(id_cmd(cmd))
        else:
            print(id_cmd(cmd))

        if error:
            print("Error: " + cmd)

        else:
            if listen:
                again = true_false("Another command? ")
                if again:
                    error, cmd = listener.listen()
                else:
                    cmd = ""
            else:
                cmd = input("Command: ")

    if speak:
        speaker.remove_files()

    # old way checking at the start
    """
    if listen and speak:    #speaking and listening

        while cmd != "" and not error:
            error, cmd = speaker.speak(id_cmd(cmd))
            if not error:
                again = true_false("Another command? ")
                if again:
                    error, cmd = listener.listen()
                else:
                    cmd = ""
        
        speaker.remove_files()

    elif listen:            #listening but not speaking

        while cmd != "" and not error:
            print(id_cmd(cmd))
            again = true_false("Another command? ")
            if again:
                error, cmd = listener.listen()
            else:
                cmd = ""
    
    elif speak:             #speaking but not listening
    
        while cmd != "" and not error:
            error, cmd = speaker.speak(id_cmd(cmd))
            if not error:
                cmd = input("Command: ")
        
        speaker.remove_files()

    else:                   #neither

        while cmd != "":
            print(id_cmd(cmd))
            cmd = input("Command: ")
    
    if error:
        print("Error: " + cmd)
    """

if __name__ == "__main__":
    from JarvisAndroid import init_Jarvis_android as r
    r(True, True)
