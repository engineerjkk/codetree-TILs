import sys
input = sys.stdin.readline
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
max_cnt=0
for i in range(n):
    for j in range(n-2):
        max_cnt=max(max_cnt,space[i][j]+space[i][j+1]+space[i][j+2])
print(max_cnt)