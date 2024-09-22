import statistics as st
import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    s=[]
    for i in range(n):
        s+=[values[i]]*freq[i]
    s.sort()
    l =len(s)
    
    if l%2==0:
        lower_half =s[:l//2]
        upper_half =s[l//2:]
    else:
        lower_half =s[:l//2]
        upper_half =s[l//2+1:]
        
    q1=st.median(lower_half)
    q3=st.median(upper_half)
    
    interquartile_range = round(float(q3-q1),1)
    print(interquartile_range)
    # Print your answer to 1 decimal place within this function

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
