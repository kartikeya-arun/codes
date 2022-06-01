#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    m=n
    while(m%3!=0):
        m-=5
    if(m<0):
        return '-1'
    else:
        return (m*'5'+(n-m)*'3')
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        print(decentNumber(n))
