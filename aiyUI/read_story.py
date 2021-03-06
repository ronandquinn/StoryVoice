#!/usr/bin/env python3

"""StoryVoice machine learning original story generation system"""
"""Main system UI menu"""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import time
import string
import os
import sys
import sqlite3
from new_story import new_story
from db import saved_story
from db import manage
from helper import end

# menu prints options and inputs to screen to eleviate possible hardware based, audio UI issues
def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('new')
    recognizer.expect_phrase('old')
    recognizer.expect_phrase('manage')
    recognizer.expect_phrase('quit')
    recognizer.expect_phrase('one')
    recognizer.expect_phrase('two')
    recognizer.expect_phrase('three')
    recognizer.expect_phrase('four')
    recognizer.expect_phrase('five')
    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()
    while True:
        print('Press the button and speak')
        button.wait_for_press()
        led.set_state(aiy.voicehat.LED.ON)
        time.sleep(1)
        aiy.audio.say('Would you like a new story, old story, to manage your stories, or quit?')
        print('Would you like a new story, old story, to manage your stories, or quit? ')
        print('Please answer "new", "old", "manage" or "quit"')
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
            if 'new' in text:
                led.set_state(aiy.voicehat.LED.ON)
                aiy.audio.say('OK, I am making up a story for you, just let me think of one...')
                led.set_state(aiy.voicehat.LED.OFF)
                print('Thinking...')
                new_story()
            elif 'old' in text:
                led.set_state(aiy.voicehat.LED.ON)
                aiy.audio.say('OK, tell me the number of the story you want to hear?')
                print('Please answer with the number only')
                led.set_state(aiy.voicehat.LED.OFF)
                print('Listening...')
                led.set_state(aiy.voicehat.LED.BLINK)
                story = recognizer.recognize()
                led.set_state(aiy.voicehat.LED.OFF)
                if not story:
                    led.set_state(aiy.voicehat.LED.ON)
                    aiy.audio.say('Sorry, I did not hear you.')
                    led.set_state(aiy.voicehat.LED.OFF)
                else:
                    print('You said " number', story, '"')
                    led.set_state(aiy.voicehat.LED.ON)
                    aiy.audio.say('OK, I will look up story number "' + story + '", it will just take a minute')
                    led.set_state(aiy.voicehat.LED.OFF)
                    saved_story(story)
            elif 'manage' in text:
                led.set_state(aiy.voicehat.LED.OFF)
                manage()
            elif 'quit' in text:
                led.set_state(aiy.voicehat.LED.OFF)
                end()

if __name__ == '__main__':
    main()
