import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    total = 0
    chunk_dic = {}
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            words = s[j:j + i]
            chunk = ''.join(sorted(s[j:j + i]))
            total += chunk_dic.setdefault(chunk, 0)
            chunk_dic[chunk] += 1
    return total

if __name__ == '__main__':
    sys.stdin = open('input.txt','r')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

