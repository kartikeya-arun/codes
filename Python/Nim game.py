#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    result=0
    for i in range(len(pile)):
        result=result^pile[i]
    return ('Second' if result==0 else 'First')
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        fptr.write(result + '\n')

    fptr.close()
