def is_right(u):
    stack = 0
    for idx in range(len(u)):
        if u[idx] == '(':
            stack += 1
        elif u[idx] ==')':
            stack -= 1
            if stack <0 :
                return False
    if stack == 0: return True

def make_right(u,v):
    right = '('
    right += solution(v)
    right += ')'
    u = u[1:-1]
    for i in u:
        if i == '(':
            right += ')'
        else:
            right += '('
    return right

def solution(p):
    answer = ''
    lenp = len(p)
    if lenp <2:
        return answer

    u,v = '',''
    cnt = 0

    for idx in range(lenp):
        u += p[idx]
        if p[idx] == '(':
            cnt += 1
        elif p[idx] == ')':
            cnt -= 1
        if cnt == 0:
            if idx != 0:
                v = p[idx+1:]
                break

    if is_right(u):
        answer = u + solution(v)
    else:
        answer =make_right(u,v)

    return answer

import sys
sys.stdin = open('input.txt','r')

p = input()
print(solution(p))
