# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
import random
import pyperclip
import os
import requests


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)





# Online sheet

def getInsultsFromUrl(url):
    response = requests.get(url)
    assert response.status_code == 200, 'Wrong status code'
    data = str(response.content)

    data = data.split('dir="ltr">')
    data = data[4:-2]

    insults = []
    for word in data:
        word = word.split("<")[0]
        if word.strip():
            insults.append(word.strip())

    return insults


if not os.path.exists("insults.txt"):
    with open("insults.txt", "w") as f:
        f.write("dumbass")


with open("insults.txt", "r") as f:
    insults = f.read().split("\n")

    if "" in insults:
        insults.remove("")

    if "docs.google.com" in insults[0]:
        insults = getInsultsFromUrl(insults[0])




if not os.path.exists("badwords.txt"):
    open("badwords.txt", "w")

if not os.path.exists("cmds.txt"):
    with open("cmds.txt", "w") as f:
        f.write("summon fireball ~ ~1 ~ {ExplosionPower:4,Motion:[0.0,-3.0,0.0]}")

with open("badwords.txt", "r") as f:
    badwords = f.read().split("\n")

    if "" in badwords:
        badwords.remove("")


with open("cmds.txt", "r") as f:
    cmds = f.read().split("\n")

    if "" in cmds:
        cmds.remove("")

if not insults:
    print("COULD NOT CONNECT TO INSULTS LIST!")

# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init()

def SpeakText(command):
    # Initialize the engine
    engine.say(command)
    engine.runAndWait()

def runCmd():
    #print(cmds)
    randomlyPickedCommand = random.choice(cmds)
    if randomlyPickedCommand[0] == "/":
        randomlyPickedCommand = randomlyPickedCommand[1:]
    pyperclip.copy(randomlyPickedCommand)
    os.system(resource_path("Minecraft.exe"))

print("Now listening!")
print("...")

while True:

    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2, phrase_time_limit=7)

            # Using google to recognize audio
            audioText = r.recognize_google(audio2)
            audioText = audioText.lower()

            print(audioText)

            # check if bad word is in audioText
            for word in badwords:
                if word in audioText:
                    #sendToDiscord()
                    runCmd()
                    announceText = "You said %s, %s" % (word, random.choice(insults))
                    SpeakText(announceText)
                    break

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        pass