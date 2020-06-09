import os
import webbrowser
import random
from gtts import gTTS 

x = True
def getReply(message):
    #Alice asking the person for help. 
    if 'hi' in message or 'Hi' in message or 'Hello' in message or 'hello' in message:
        reply = "How may I help you?"
        print('Alice: '+reply)
        
        mytext = 'How may I help you?'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        
    #Question 1
    elif 'new Project' in message or 'New Project' in message:
        reply = "This is the answer for Question 1"
        print('Alice: '+reply)
        
        mytext = 'This is the answer for Question 1'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
    
    #Question 2
    elif 'progress report' in message or 'last progress' in message:
        reply = "This is the answer for Question 2"
        print('Alice: '+reply)
        
        mytext = 'This is the answer for Question 2'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
        
    #Question 3
    elif '% progress' in message:
        reply = "This is the answer for Question 3"
        print('Alice: '+reply)
        
        mytext = 'This is the answer for Question 3'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
    
    #Question 4
    elif 'Discipline engineers' in message or 'engineers contact details' in message:
        reply = "This is the answer for Question 4"
        print('Alice: '+reply)
        
        mytext = 'This is the answer for Question 4'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
    
    #Question 5
    elif 'target' in message or 'on target' in message:
        reply = "This is the answer for Question 5"
        print('Alice: '+reply)
        
        mytext = 'This is the answer for Question 5'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
        
    
    elif 'bye' in message or 'Bye' in message:
        reply = "Thank You. It was nice talking to you"
        print('Alice: '+reply)
        
        mytext = 'Thank You. It was nice talking to you'
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False) 
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
        
        exit()
        
    
    else:
        reply = "I am sorry. I can't understand you"
        print('Alice: '+reply)
        
        
        mytext = "I am sorry. I can't understand you"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("output.mp3")
        os.system("start output.mp3")
        print('\n')
    
    
#Driver Program 
print("Alice: Greetings of the day. I am Alice, your personal assistant. Can I know your name?")
mytext = "Greetings of the day. I am Alice, your personal assistant. Can I know your name?"
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3")
os.system("start output.mp3")
print('\n')

name = input('Human: ')
print("Alice: Hello ",end = '')
print(name, end = '')
print(". How can I help you?")

mytext = "How can I help you?"
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3")
os.system("start output.mp3")
print('\n')

while(x == True):
    message = input('Human: ')
    getReply(message)