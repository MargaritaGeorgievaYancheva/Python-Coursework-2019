#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(array):
    sum=0
    for i in (array):
     sum+=i
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    array = list(map(int, input().rstrip().split()))

    result = simpleArraySum(array)

    fptr.write(str(result) + '\n')

    fptr.close()
