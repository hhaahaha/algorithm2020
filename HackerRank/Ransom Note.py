import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag = {}
    for magWord in magazine:
        mag.setdefault(magWord,0)
        mag[magWord]+=1

    for noteWord in note:
        mag.setdefault(noteWord,0)
        if mag[noteWord] == 0:
            return 'No'
        else:
            mag[noteWord] -= 1

    return 'Yes'


if __name__ == '__main__':
    sys.stdin = open('input.txt','r')
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()
    print(magazine)

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
