# StoryVoice - Ronan Quinn D15124865

aiyUI is the software installed on the project's Google AIY voice kit hardware
It is installed at path:
home/pi/AIY-voice-kit-python/src/examples/voice/

Included in aiyUI is the getstory.sh script, which launches the scripts for making an ssh connection to the
gcpInstance, and for moving the generated story back to the AIY

aiyUI is launched by opening a terminal on the AIY, navigating to the path noted above, and entering:

"python3 read_story.py"

The UI is audio based, and offers newly generated stories, story saving option, retrieval of previously saved stories
and SQLite database management options
