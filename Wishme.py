
import time
import pyttsx3

Waqt=int(time.strftime('%H')) 
oreo=pyttsx3.init()

def OreoSay(audio):
    oreo.say(audio)
    oreo.runAndWait()

def wishme():
    if(Waqt>=0 and 12>=Waqt):
        oreosay(f'''Good morning,{name}! I hope you slept well and woke up feeling refreshed and 
        ready to take on the day. May this morning bring you the energy and positivity you need to 
        accomplish your goals and make the most of every moment. Remember to take some time for yourself 
        today and enjoy the little things that bring you happiness. Have a wonderful day ahead!''')
    elif(Waqt>=12 and 16>=Waqt):
        OreoSay(f'''Good afternoon, {name}! I hope your day has been going well so far. 
        Whether you've been busy with work or enjoying some leisure time, 
        I hope you've been able to find moments of joy and fulfillment. As we move into the afternoon, 
        may your focus and productivity remain strong, and may you continue to make progress towards your goals.
        Take a break when you need it, and remember to take care of yourself.
         Wishing you a happy and successful rest of the day!''')
    elif(Waqt>=16 and 20>=Waqt): 
        OreoSay(f"Good Evening{name}")   
    else:
        OreoSay(f"""Hey {name}, it's time to wind down and get some rest. I hope today brought you joy, happiness, 
        and fulfillment. As you prepare to end the day, take a moment to reflect on all the good things that happened, 
        and let go of any negativity that may be weighing you down. 
        Close your eyes, breathe deeply, and let your mind and body relax. 
        May you have a peaceful and restful night's sleep, and wake up tomorrow 
        feeling refreshed and ready to tackle whatever comes your way.
        Good Night....Sweet dreams, {name}!""")
        

print('Enter your Name: ')
name=input()
wishme()


