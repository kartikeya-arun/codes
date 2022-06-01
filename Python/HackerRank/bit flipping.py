#!/bin/python3

# You will be given a list of 32 bit unsigned integers. Flip all the bits

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    return n^(2**32-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
