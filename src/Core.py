from datetime import datetime
from random import choice
from Util import suffix
import IO
import logging

class Jarvis:
    def __init__(self):
        logging.info("Jarvis instance started")

    def respond(self, cmd: str) -> str:

        # format cmd to remove punctuation
        cmd = " " + cmd.lower() + " "
        allowed_chrs = "abcdefghijklmnopqrstuvwxyz1234567890 "
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
                    hours = datetime.now().hour
                    if hours < 12:
                        out = "Good morning"
                    elif hours < 18:
                        out = "Good afternoon"
                    else:
                        out = "Good evening"
                
            elif " time " in cmd and " what " in cmd:
                now = datetime.now()
                out = "it is {}:{}".format(now.hour, now.minute)
                
            elif " what" in cmd and (" day " in cmd or " date " in cmd or " year " in cmd or " month " in cmd):

                now = datetime.now()
                out = now.strftime("it is %A the {}{} of %B %Y".format(now.day, suffix(now.day)))
    
            else:
                out = "I don't know what you mean by that"
        
        return out

def main(inputter, outputter):
    """
    Run Jarvis with the given inputter and outputter which
    are system specific
    """

    jarvis = Jarvis()
    cmd = inputter.input_()
    while cmd != "":
        response = jarvis.respond(cmd)
        outputter.output(response)
        cmd = inputter.input_()
