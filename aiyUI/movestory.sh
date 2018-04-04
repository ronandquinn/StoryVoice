#!/bin/bash
# script moves newly generated story from gcpInstance to AIY for reading
# requires googles gcloud sdk 
gcloud compute scp ronanq@story-creator:~/DeepWriting1/new.txt /home/pi/AIY-voice-kit-python/src/examples/voice/StoryVoice
