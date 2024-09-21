#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    mean=sum(vals)/n
    variance=sum([((val-mean)**2)for val in vals])/n
    stddev=variance**0.5
    print("{0:0.1f}".format(stddev))
    # Print your answers to 1 decimal place within this function

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
