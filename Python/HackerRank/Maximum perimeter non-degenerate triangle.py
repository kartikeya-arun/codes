#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    # Logic : Select the longest possible side such that it can form a non-degenerate triangle using the two sides "just smaller" than it.
    # It fulfills all other conditions. If no such selection is possible, then no non-degenerate triangle exists.
    sticks.sort()
    n=len(sticks)
    i=n-3
    while i>=0 and (sticks[i]+sticks[i+1]<=sticks[i+2]):
        i-=1
    if i>=0:
        return (sticks[i],sticks[i+1],sticks[i+2])
    else:
        return [-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
