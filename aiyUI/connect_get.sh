#!/bin/bash
# script makes ssh connection to gcpInstance engine
# change directory to the DeepWriting model
# run sample.py to generate new story, then exits
gcloud compute ssh ronanq@story-creator --zone=us-east1-b << EOF
cd DeepWriting1
python sample.py
exit
EOF
