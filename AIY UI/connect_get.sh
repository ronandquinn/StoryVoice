#!/bin/bash
gcloud compute ssh ronanq@story-creator --zone=us-east1-b << EOF
cd DeepWriting1
python sample.py
exit
EOF

