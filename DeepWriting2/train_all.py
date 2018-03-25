import os
s = 1
while s < 650:
    os.system("python train.py --input_file story%s.txt" % s)
    s += 1
