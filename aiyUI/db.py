 #!/usr/bin/env python3
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import sqlite3
import string
import sys
import os

from helper import text2int
from helper import read
from helper import end
from helper import strip_punct

punct=["'", "`", "-", "*", "[", "]"]
button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()
recognizer = aiy.cloudspeech.get_recognizer()
conn = sqlite3.connect('stories.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stories (name TEXT, content TEXT)")
conn.commit()

s = 1

def manage():
    recognizer.expect_phrase('How many')
    recognizer.expect_phrase('delete')
    recognizer.expect_phrase('clear')
    recognizer.expect_phrase('go back')

    while True:
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say('Would you like to know how many you have, delete a story, clear the list, or go back')
        print('How many, delete, clear or go back?')
        led.set_state(aiy.voicehat.LED.OFF)
        print('Listening...')
        led.set_state(aiy.voicehat.LED.BLINK)
        text = recognizer.recognize()
        led.set_state(aiy.voicehat.LED.OFF)
        if not text:
            led.set_state(aiy.voicehat.LED.ON)
            aiy.audio.say('Sorry, I did not hear you.')
            led.set_state(aiy.voicehat.LED.OFF)
        else:
            print('You said "', text, '"')
            if 'many' in text:
                how_many()
                led.set_state(aiy.voicehat.LED.ON)
                aiy.audio.say("You have %s saved stories" % m)
                led.set_state(aiy.voicehat.LED.ON)
                return
            elif 'delete' in text:
                delete()
                return
            elif 'clear' in text:
                clear()
                return
            elif 'back' in text:
                return
    return

def save_story(sv):
    global s
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say("OK, saving as story number%s" % s)
    led.set_state(aiy.voicehat.LED.OFF)
    os.rename(sv , 'story%s.txt' % s)
    svd = ('story%s.txt' % s)
    c.execute("CREATE TABLE IF NOT EXISTS stories (name TEXT, content TEXT)")
    conn.commit()
    name = svd
    with open(svd, "r") as f:
        content = f.read()
    c.execute("INSERT INTO stories (name, content) VALUES(?, ?)", (name, content))
    conn.commit()
    s += 1
    return

def saved_story(story):
    a = text2int(story)
    name = ('story%s.txt' % a)
    print("Looking up", name)
    if c.execute("SELECT content FROM stories WHERE name = ?", (name,)):
        t = c.fetchone()
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say("Ok, here's your story")
        led.set_state(aiy.voicehat.LED.OFF)
        p = strip_punct(t)
        read(p)
    else:
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say("Sorry, I can't find that story")
        led.set_state(aiy.voicehat.LED.OFF)
    return

def how_many():
    c.execute("CREATE TABLE IF NOT EXISTS stories (name TEXT, content TEXT)")
    conn.commit()
    c.execute("SELECT * FROM stories")
    m = len(c.fetchall())
    return m

def delete():
    recognizer.expect_phrase('one')
    recognizer.expect_phrase('two')
    recognizer.expect_phrase('three')
    recognizer.expect_phrase('four')
    recognizer.expect_phrase('five')
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say('OK, tell me the number of the story you want to delete?')
    led.set_state(aiy.voicehat.LED.OFF)
    print('Listening...')
    led.set_state(aiy.voicehat.LED.BLINK)
    deS = recognizer.recognize()
    led.set_state(aiy.voicehat.LED.OFF)
    if not deS:
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say('Sorry, I did not hear you.')
        led.set_state(aiy.voicehat.LED.OFF)
    else:
        print('You said "', deS, '"')
        a = text2int(deS)
        name = ('story%s.txt' % a)
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say("Ok, deleting story number %s" % a)
        led.set_state(aiy.voicehat.LED.OFF)
        c.execute("DELETE FROM stories WHERE name = ?", (name,))
        conn.commit()
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say("Story number %s deleted" % a)
        led.set_state(aiy.voicehat.LED.OFF)
    return

def clear():
    global s
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say("Clearing out all stories")
    led.set_state(aiy.voicehat.LED.OFF)
    c.executescript('DROP TABLE IF EXISTS stories;')
    conn.commit()
    s = 1
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say("Ok, all stories have been deleted")
    led.set_state(aiy.voicehat.LED.OFF)
    return

def back():
    return 

