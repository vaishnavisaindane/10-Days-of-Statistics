from statistics import median
import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr.sort()
    n = len(arr)
   
    Q2 = int(median(arr))
    
    if n % 2 == 0:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2:]
    else:
        lower_half = arr[:n // 2]
        upper_half = arr[n // 2 + 1:]
    
    Q1 = int(median(lower_half))
    Q3 = int(median(upper_half))
    
    return [Q1, Q2, Q3]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
