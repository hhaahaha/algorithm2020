
import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    i = -1
    memo = {}
    while i < len(q)-2:
        i += 1
        i = max(0,i)
        if q[i] == i+1:
            continue

        if q[i]> q[i+1]:
            if memo.setdefault(q[i],0) == 2:
                return 'Too chaotic'
            memo[q[i]] += 1
            q[i], q[i+1] = q[i+1], q[i]
            i -=2
    return sum(memo.values())

if __name__ == '__main__':
    sys.stdin = open('input.txt','r')
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
