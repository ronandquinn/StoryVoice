#!/usr/bin/env python3
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import string
import sys
import os
from helper import read
from db import save_story
from helper import end

def new_story():
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('no thanks')
    recognizer.expect_phrase('yes please')
    os.system("./getstory.sh")
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say("OK, here's my latest story")
    led.set_state(aiy.voicehat.LED.OFF)
    with open('new.txt') as f:
        t = f.read()
        read(t)
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say("Would you like to save this story to hear it again?")
    led.set_state(aiy.voicehat.LED.BLINK)
    print('Listening...')
    ans = recognizer.recognize()
    led.set_state(aiy.voicehat.LED.OFF)
    if not ans:
        led.set_state(aiy.voicehat.LED.ON)
        aiy.audio.say('Sorry, I did not hear you.')
        led.set_state(aiy.voicehat.LED.OFF)
    else:
        print('You said "', ans, '"')
        if 'no' in ans:
            return
        if 'yes' in ans:
            sv = ('new.txt')
            save_story(sv)
            return

