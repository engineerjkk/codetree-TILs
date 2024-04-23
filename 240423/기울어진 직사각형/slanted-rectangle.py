import sys
input = sys.stdin.readline
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

def in_range(x,y):
    return -1<x<n and -1<y<n

def score(i,j,k,l):
    drs=[-1,-1,1,1]
    dcs=[1,-1,-1,1]
    moves=[k,l,k,l]
    nm=0
    for dr,dc, move in zip(drs,dcs,moves):
        for num in range(move):
            i=i+dr
            j=j+dc
            if not in_range(i,j):
                return 0
            nm+=space[i][j]
    return nm

ans=0
for i in range(n):
    for j in range(n):
        for k in range(1,n):
            for l in range(1,n):
                value = score(i,j,k,l)
                ans=max(ans,value)
print(ans)