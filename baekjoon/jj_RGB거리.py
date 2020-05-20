import sys

sys.stdin = open('input.txt','r')
N = int(input())
RGB_cost = [[0,0,0]] + [list(map(int,input().split())) for _ in range(N)]

DP = [[0,0,0] for _ in range(N+1)] #0 인덱스 추가

for idx in range(1,N+1):
    curr_rgb = [0, 0, 0]
    curr_rgb[0] = min(RGB_cost[idx][0] + DP[idx-1][1], RGB_cost[idx][0] + DP[idx-1][2])
    curr_rgb[1] = min(RGB_cost[idx][1] + DP[idx-1][0], RGB_cost[idx][1] + DP[idx-1][2])
    curr_rgb[2] = min(RGB_cost[idx][2] + DP[idx-1][0], RGB_cost[idx][2] + DP[idx-1][1])

    DP[idx] = curr_rgb

print(min(DP[-1]))



