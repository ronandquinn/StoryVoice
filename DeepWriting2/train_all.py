# Ensure save directory has been cleared before execution
# Only set while loop to 4-6 for brevity, while testing
# Reset to 649, only when ready for full training
# Reset retrain.py to train.py when ready for full training
# Once started, ctrl+C must be executed 648 times if you wish to stop

import os
s = 4
os.system("python train.py --input_file story%s.txt" % s)
s += 1
while s < 6:
    os.system("python train.py --input_file story%s.txt --init_from save" % s)
    s += 1
