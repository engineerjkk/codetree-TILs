import sys
input=sys.stdin.readline
n,m = map(int,input().split())

space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

def in_range(x,y):
    return -1<x<n and -1<y<m

def score(i,j,k,l):
    drs=[1,0,-1,0]
    dcs=[0,-1,0,1]
    moves=[k,l,k,l]
    nm=0
    for dr,dc,move in zip(drs,dcs,moves):
        i=i+dr
        j=j+dc
        if not in_range(i,j):
            return 0
        nm+=space[i][j]
    return nm

def score2(i,j,k,l,visited):
    drs=[0,-1,0,1]
    dcs=[1,0,-1,0]
    moves=[k,l,k,l]
    nm=0
    for dr,dc,move in zip(drs,dcs,moves):
        i=i+dr
        j=j+dc
        if not in_range(i,j) or visited[i][j]==True:
            return 0
        nm+=space[i][j]
    return nm



ans1=-sys.maxsize
visited=[[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        for k in range(1,n):
            for l in range(1,m):
                value=score(i,j,k,l)
                if value>ans1:
                    ans1=value
                    visited=[[False]*m for _ in range(n)]
                    for row in range(i,k+1):
                        for col in range(j,l+1):
                            visited[row][col]=True
ans2=-sys.maxsize
for i in range(n):
    for j in range(m):
        for k in range(1,n):
            for l in range(1,m):
                value=score2(i,j,k,l,visited)
                ans2=max(ans2,value)
                    
print(ans1+ans2)