 #!/usr/bin/env python3
import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import sqlite3
import string
import sys
import os

punct=["'", "`", "-", "*", "[", "]", "(", ")", '"']
button = aiy.voicehat.get_button()
led = aiy.voicehat.get_led()

def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

def read(x):
    r = strip_punct(x)
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say(r)
    aiy.audio.say("The end.")
    aiy.audio.say("I hope you liked it.")
    led.set_state(aiy.voicehat.LED.OFF)
    return

def strip_punct(s):
    return "".join(c for c in s if c not in punct)

def end():
    led.set_state(aiy.voicehat.LED.ON)
    aiy.audio.say('Ok, goodbye!')
    led.set_state(aiy.voicehat.LED.OFF)
    exit()
