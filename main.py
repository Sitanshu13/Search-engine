import pyttsx3
import wikipedia
from googlesearch import search

startingMessage = 'Hello, I am your search assistant, What can I do for you: '
start = True

def searcherWiki(wikiSearch):
    speaker = pyttsx3.init()
    print(' ')
    print(wikipedia.summary(questionWiki))
    speaker.say(wikipedia.summary(questionWiki))
    speaker.runAndWait()

def searcherGoogle(googleSearch):
    speaker = pyttsx3.init()
    print(' ')
    speaker.say('These are the websites which have the information related to your search: ')
    print(search(questionGoogle))
    speaker.runAndWait()

if(start == True):
    speaker = pyttsx3.init()
    print(startingMessage)
    speaker.say(startingMessage)
    speaker.runAndWait()
    googleOrWiki = input('Do you want to use Google or Wikipedia: ')
    if(googleOrWiki == 'wiki'):
        questionWiki = input('Wikipedia Search: ')
        searcherWiki(questionWiki)
        speaker = pyttsx3.init()
    elif(googleOrWiki == 'google'):
        questionGoogle = input('Google Search: ')
        searcherGoogle(questionGoogle)
        speaker = pyttsx3.init()