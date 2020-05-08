import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    limj = len(arr)
    limi = len(arr[-1])
    totalSum = []
    for i in range(limi-2):
        for j in range(limj-2):
            hourglass = 0
            a = arr[i][j:j+3]
            b = arr[i+1][j+1]
            c = arr[i+2][j:j+3]
            hourglass = sum(a) + b + sum(c)
            totalSum.append(hourglass)
    print(max(totalSum))


if __name__ == '__main__':
    sys.stdin = open('input.txt','r')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
