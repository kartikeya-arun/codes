#!/bin/python3

# The time of delivery is calculated as the sum of the
# order number and the preparation time. If two orders are delivered at the same time,
# assume they are delivered in ascending customer number order.

# Complete the jimOrders function in the editor below. It should return an array of
# integers that represent the order that customers' orders are delivered.

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    s = sorted(enumerate(orders,1),key=lambda x:sum(x[1]))
    return [i[0] for i in s]
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
