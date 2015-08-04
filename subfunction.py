from datetime import datetime
from subprocess import call
import jmail
from os import system

def recognize(text,processor=0):
    text = text.lower()
    result = 0
    if(processor==0):
        if "search for" in text:
            call(["sr","google", " ".join(text.split()[2:])])
            return 0
        elif "search" in text and "for" in text:
            call(["sr", text.split()[1], " ".join(text.split()[3:])])
            return 0
        if "what" in text:
            if "time" in text:
                read_time()
                return 0
            if "day" in text or "date" in text:
                read_date()
                return 0
        if "check" in text and "mail" in text:
            check_mail()
            return 1
        speak("You said " + text)
        return 0
    if(processor==1):
        check_mail_follow(text)
        return 0
    
    return 0

def check_mail_follow(text):
    text = text.lower()
    if "who" in text:
        a = jmail.getDetails("from")
        for i in range(len(a)):
            a[i] = a[i].split("<")[0]
        speak("You've got mail from" + prettify_list(a))

def prettify_list(l):
    if len(l) < 2:
        return str(l)
    result = ""
    for i in range(len(l)-1):
        result += str(l[i]) + " ,"
    result+=" and" + l[-1]
    return result
        
    
def check_mail():
    unread = jmail.get_unread()
    if unread<0:
        speak("There was an error fetching your messages")
    elif unread==0:
        speak("You have no new messages")
    elif unread==1:
        speak("You have one new message")
    else:
        speak("You have " + str(jmail.get_unread()) + " new messages")
def read_time():
    dt = datetime.now()
    hrs = dt.hour%12
    mins= dt.minute
    if(mins == 0):
        mins = "o'clock"
    elif(mins<10):
        mins = "o"+str(mins)
    else:
        mins = str(mins)
    mod = " P.M." if dt.hour/12 > 1 else " A.M."
    speak(str(hrs)+" "+mins+mod)


def read_date():
    dt = datetime.now()
    m_list = "January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"
    d_list = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    month = dt.month
    date = dt.day
    if(date == 1):
        date = "first"
    elif (date == 2):
        date = "second"
    elif (date == 3):
        date = "third"
    else:
        date = str(date)+"th"
    wkdy = d_list[dt.weekday()]
    phrase =  "Today is " + d_list[dt.weekday()] + " " + m_list[month-1] + " " + date
    speak(phrase)

def speak(phrase):
    print(phrase)
    system('echo "'+phrase+'" | festival --tts') 
