import numpy as np
from scipy import stats
size=int(input())
num=list(map(int,input().split()))
print(np.mean(num))
print(np.median(num))
print(stats.mode(num)[0])
