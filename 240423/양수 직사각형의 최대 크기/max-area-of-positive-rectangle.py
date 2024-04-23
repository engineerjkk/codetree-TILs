import sys
input = sys.stdin.readline
n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

board=[[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if space[i][j]>0:
            board[i][j]=1

def check_positive(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if space[i][j]<=0:
                return False
    return True

def rec(x1,y1,x2,y2):
    nm=0
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            nm+=board[i][j]
    return nm


ans=0
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for l in range(j,m):
                if check_positive(i,j,k,l):
                    ans=max(ans,rec(i,j,k,l))
if ans<=0:
    print(-1)
else:
    print(ans)