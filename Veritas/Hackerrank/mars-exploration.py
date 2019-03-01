#!/bin/python3

import math
import os
import random
import re
import sys

s = "OOSDSSOSOSWEWSOSOSOSOSOSOSSSSOSOSOSS"
def marsExploration(s):
    counter = 0
    for i in range(0, len(s) + 1, 3):
        if s[i : i + 3] != "SOS":
            message = s[i : i + 3]
            for a in range(len(message)):
                if a == 0:
                    if message[a] != "S":
                        counter += 1
                        continue
                    else:
                        continue
                if a == 2:
                    if message[a] != "S":
                        counter += 1
                        continue
                    else:
                        continue
                else:
                    if message[a] != "O":
                        counter += 1
                        continue
                    else:
                        continue
    return counter
print(marsExploration(s))
