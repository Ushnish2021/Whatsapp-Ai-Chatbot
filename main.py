import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)


position1 = pt.locateOnScreen("Smily_Paperclip.jpeg", confidence= .9)
x = position1[0]
y = position1[1]

#Gets Message
def get_message():
    global x,y
    

    position = pt.locateOnScreen("Smily_Paperclip.jpeg", confidence= .9)

    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration =.5)
    pt.moveTo(x+190, y-60, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(11,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    print("Message received:" + whatsapp_message)

    return whatsapp_message

def post_response(message):
    global x, y
    position = pt.locateOnScreen("Smily_Paperclip.jpeg", confidence= .9)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval =.01)
    pt.typewrite("\n", interval=.01)


def process_response(message):

    random_no=random.randrange(3)
    if "haii" in str(message).lower():
        return " Ki hoeche bolo?...This is Ushnish Ghosal's AI"
    else:
        if random_no == 0:
            return "Ushnish is not available.. I am his Chatbot"
        elif random_no == 1:
            return "Ushnish is not available.. I am his Chatbot"
        else:
            return "Ushnish will join in soon and answer... He is at present offline. I am his Chatbot"

def check_for_new_message():
    pt.moveTo(x+50,y-40, duration=.5)

    while True:
        #continuos check for green dot
        try:
            position=pt.locateOnScreen("Green_dot.jpeg", confidence=.9)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        
        
        
        except(Exception):
            print("No new messages")

        if pt.pixelMatchesColor(int(x+20),int(y-40),(0,0,0), tolerance=100):
            print("It is White")
            processed_response = process_response(get_message())
            post_response(processed_response)
        else:
            print("no new messages yet...")
            sleep(5)

            
check_for_new_message()