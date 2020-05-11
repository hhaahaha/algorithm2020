import sys

sys.stdin = open('input.txt','r')

#1
t = int(input())

for _ in range(t):
    stack = []
    VPS = False
    string = input()
    n = len(string)
    idx = 0
    while idx < n:
        i = string[idx]
        if i == ')':
            if not stack:
                VPS = False
                break
            else:
                stack.pop()
                VPS = True
        elif i == '(':
            stack.append(i)
            VPS = False

        idx += 1

    if stack: VPS = False

    if VPS:
        print('YES')
    else:
        print('NO')


#2
t = int(input())

for _ in range(t):
    stack = 0
    string = input()
    for i in string:
        if i == ')':
            stack -= 1
            if stack < 0:
                break
        elif i == '(':
            stack += 1

    if stack ==0 : print('YES')
    else: print('NO')


