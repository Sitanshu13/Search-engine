import pyttsx3
import wikipedia
from googlesearch import search
from GoogleNews import GoogleNews
import webbrowser
import datetime
import playsound

googlenews = GoogleNews()

startingMessage = 'Hello, I am your assistant, What can I do for you: '
start = False
Password = '8823'
passdenied = 5
ctime = datetime.datetime.now()
time = str(ctime.strftime("%H:%M"))

date = str(ctime.strftime("%m/d/y"))

googlenews.setlang('en')
googlenews.setperiod('d')
googlenews.setTimeRange(date,date)
googlenews.setencode('utf-8')

speaker = pyttsx3.init()
speaker.say('Please enter the password')
speaker.runAndWait()

def password():
    speaker = pyttsx3.init()
    speaker.say('Please type in the password')
    cPassword = input('Enter Password: ')
    speaker.runAndWait()
    if(cPassword == Password):
        speaker.say('Access accepted')
        speaker.runAndWait()
    else:
        speaker.say('Access denied')
        speaker.runAndWait()

def searcherWiki(wikiSearch):
    speaker = pyttsx3.init()
    print(' ')
    print(wikipedia.summary(questionWiki))
    speaker.say(wikipedia.summary(questionWiki))
    speaker.runAndWait()

def searcherGoogle(googleSearch):
    speaker = pyttsx3.init()
    print(' ')
    speaker.say('These are the websites that came according to your search')
    print(search(questionGoogle))
    speaker.runAndWait()

def calculator(calclator1):
  if(calclator1 == '1'):
      speaker = pyttsx3.init()
      add1 = int(input('Add this: '))
      add2 = int(input('To this: '))
      ans1 = add1 + add2
      print(ans1)
      speaker.say(ans1)
      speaker.runAndWait()
  elif (calclator1 == '2'):
      speaker = pyttsx3.init()
      sub1 = int(input('Subtract this: '))
      sub2 = int(input('From this: '))
      ans2 = (sub1 - sub2)
      print(ans2)
      speaker.say(ans2)
      speaker.runAndWait()
  elif (calclator1 == '3'):
      speaker = pyttsx3.init()
      mul1 = int(input('Multiply this: '))
      mul2 = int(input('Into this: '))
      ans3 = mul1 * mul2
      print(ans3)
      speaker.say(ans3)
      speaker.runAndWait()
  elif (calclator1 == '4'):
      speaker = pyttsx3.init()
      div1 = int(input('Divide this: '))
      div2 = int(input('By this: '))
      ans4 = div1 / div2
      print(ans4)
      speaker.say(ans4)
      speaker.runAndWait()

def song(playSong):
    speaker = pyttsx3.init()

    if (playSong == 'ws'):
        speaker.say("playing watermelon sugar")
        speaker.runAndWait()
        playsound.playsound("ws.mp3")

cPassword = input('Enter Password: ')
speaker.runAndWait()
if(cPassword == Password):
    speaker.say('Access accepted')
    speaker.runAndWait()
    start = True
    if (start == True):
        print(startingMessage)
        speaker.say(startingMessage)
        speaker.runAndWait()
        speaker.say('Do you want to use Google, Wikipedia, Calculator or Google News or do you want to use the link redirector or know the time or even listen to a song: ')
        speaker.runAndWait()
        googleOrWiki = input('What would you like to use: ')
        if (googleOrWiki == 'wiki'):
            questionWiki = input('Wikipedia Search: ')
            searcherWiki(questionWiki)
        elif (googleOrWiki == 'google'):
            questionGoogle = input('Google Search: ')
            searcherGoogle(questionGoogle)
        elif (googleOrWiki == 'gnews'):
            googlenews.search('APPL')
            news = googlenews.gettext()
            print(news)
            speaker.say(news)
            speaker.runAndWait()
        elif (googleOrWiki == 'link'):
            speaker.say("Would you like to go to an .org site or .com site")
            speaker.runAndWait()
            siteExt = input("Site extention: ")
            if(siteExt == '.org'):
                speaker.say('What website(.org) would you like to open? ')
                speaker.runAndWait()
                orglinkSearch = input('Website name: ')
                webbrowser.open('https://' + orglinkSearch + '.org')
            elif(siteExt == 'org'):
                speaker.say('What website(.org) would you like to open? ')
                speaker.runAndWait()
                orglinkSearch = input('Website name: ')
                webbrowser.open('https://' + orglinkSearch + '.org')
            elif (siteExt == '.com'):
                speaker.say('What website(.com) would you like to open? ')
                speaker.runAndWait()
                comlinkSearch = input('Website name: ')
                webbrowser.open('https://' + comlinkSearch + '.com')
            elif (siteExt == 'com'):
                speaker.say('What website(.com) would you like to open? ')
                speaker.runAndWait()
                comlinkSearch = input('Website name: ')
                webbrowser.open('https://' + comlinkSearch + '.com')
        elif (googleOrWiki == 'calc'):
            print('Which operation would you like to perform, Press 1 to perform addition, 2 to perform subtraction, 3 to perform multiplication and 4 to perform division')
            operation = input('Operation: ')
            calculator(operation)
        elif (googleOrWiki == 'time'):
            print(time)
            speaker.say('The current time is: ' + time)
            speaker.runAndWait()
        elif (googleOrWiki == 'date'):
            ctime = datetime.datetime.now()
            date = str(ctime.strftime("%d-%m-%y"))
            print(date)
            speaker.say("The today's date is: " + date)
            speaker.runAndWait()
        elif (googleOrWiki == 'song'):
            speaker = pyttsx3.init()
            speaker.say("What song would you like to hear to")
            speaker.runAndWait()
            songName = input("What song would you like to hear to: ")
            song(songName)

elif(cPassword != Password):
    speaker.say('Access denied')
    speaker.runAndWait()
