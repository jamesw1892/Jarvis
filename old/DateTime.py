from datetime import datetime

class CurrentDateTime():
    """
    Class to get different attributes of the current date and time in a useable format.
    """

    def __init__(self):
        self.date_time = datetime.now()
    
    def get_whole_date(self):
        return(str(self.date_time).split(" ")[0].split("-"))
    
    def get_whole_time(self):
        return(str(self.date_time).split(" ")[1].split(":"))
    
    def get_year(self):        
        return(self.get_whole_date()[0])
    
    def get_month(self):
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        return(months[int(self.get_whole_date()[1])-1])
    
    def get_date(self):
        return(str(int(self.get_whole_date()[2])))
    
    def get_day(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return(days[self.date_time.weekday()])
    
    def get_hours(self):
        return(str(int(self.get_whole_time()[0])))
    
    def get_minutes(self):
        return(str(int(self.get_whole_time()[1])))
    
    def get_seconds(self):
        return(str(round(float(self.get_whole_time()[2]))))
    
    def get_time_clock(self, hour_clock):
        """
        - hour_clock (integer): Either '12' for 12 hour clock or '24' for 24 hour clock.
        """
        
        whole_time = self.get_whole_time()
        
        hours = int(whole_time[0])
        if hours > 12 and hour_clock == 12:
            hours -= 12

        return(str(hours) + ":" + whole_time[1])
    
    def get_date_digits(self, style):
        """
        - style (string): Either 'UK' or 'US' and this determines whether the day or the month comes first.
        """

        whole_date = self.get_whole_date()
        
        if style.upper() == "UK":
            date_digits = whole_date[2] + "/" + whole_date[1] + "/" + whole_date[0]
        elif style.upper() == "US":
            date_digits = whole_date[1] + "/" + whole_date[2] + "/" + whole_date[0]
        else:
            raise ValueError("style must be either 'UK' or 'US'.")
        
        return(date_digits)
    
    def get_date_words(self):
        
        date = self.get_date()
        
        if int(date) // 10 == 1:
            suffix = "th"
        else:
            mod = int(date) % 10
            if mod == 1 and int(date):
                suffix = "st"
            elif mod == 2:
                suffix = "nd"
            elif mod == 3:
                suffix = "rd"
            else:
                suffix = "th"

        return(self.get_day() + " " + date + suffix + " " + self.get_month() + ", " + self.get_year())

def get_datetime():
    """
    Function to get the current date and time.
    ~
    RETURNS:
    - year (int): The current year.
    - month (int): The current month.
    - day (int): The current day.
    - hours (int): The current hour (24 hour).
    - minutes (int): The current minute.
    - seconds (int): The current second.
    """

    now = datetime.now()

    return now.year, now.month, now.day, now.hour, now.minute, now.second

def get_time_clock(hour_clock=12, seconds=False):
    """
    - hour_clock (integer): Either '12' for 12 hour clock or '24' for 24 hour clock.
    - seconds (boolean): Whether or not to include seconds.
    """

    now = datetime.now()

    if hour_clock == 12 and now.hour > 12:
        hours = now.hour - 12

    s = "{}:{}".format(hours, now.minute)

    if seconds:
        s += ":{}".format(now.second)

    return s

def approx(hrs, mins, secs):
    
    if (mins % 5 == 2 and secs < 30) or mins % 5 < 2:
        mins = (mins // 5) * 5
    else:
        mins = ((mins // 5) + 1) * 5

    if mins > 30:
        hrs += 1
        word = "to"
        mins = 60 - mins
    else:
        word = "past"
    
    hrs = hrs % 12
    if hrs == 0:
        hrs = 12

    if mins % 60 == 0:
        return "{} o'clock".format(hrs)
    elif mins == 30:
        return "half past {}".format(hrs)
    elif mins % 15 == 0:
        return "quarter {} {}".format(word, hrs)
    else:
        return "{} {} {}".format(mins, word, hrs)

#print(approx(int(input("hrs: ")), int(input("mins: ")), int(input("secs: "))))

if __name__ == "__main__":

    i = CurrentDateTime()
    print("Type 'i.' and then the function name including the brackets and any parameters to execute a function and print the result. Any other python commands will work too.")
    while True:
        print(eval(input(">>>")))