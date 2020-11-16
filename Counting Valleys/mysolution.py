#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley = 0
    sea_lvl = 0 
    for x in path:
        # if U increase sea level 
        if x == 'U':
            sea_lvl += 1
            
        # if D decrease sea level 
        elif x == 'D':
            sea_lvl -= 1
            
        # coming back to sea level 
        if sea_lvl == 0 and x == 'U':
            valley += 1
            
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
