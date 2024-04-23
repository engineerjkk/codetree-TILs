import sys
input = sys.stdin.readline

n = int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

def in_range(r,c):
    return -1<r<n and -1<c<n

def score(i,j,k,l):
    drs=[-1,-1,1,1]
    dcs=[1,-1,-1,1]
    move_nums=[k,l,k,l]
    nm=0
    for dr,dc,move_num in zip(drs,dcs,move_nums):
        for _ in range(move_num):
            i=i+dr
            j=j+dc
            if not in_range(i,j):
                return 0
            nm+=space[i][j]
    return nm

answer=0
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            for l in range(1,n):
                value=score(i,j,k,l)
                answer=max(answer,value)
print(answer)