#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i < j:
            if i != 8 or j != 9:
                print("{:02d}, ".format(i * 10 + j), end="")
            else:
                print("{:02d}".format(i * 10 + j))
