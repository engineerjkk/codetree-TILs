import sys
input = sys.stdin.readline

n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

def shape1(space,r,c):
    dr=[[-1,0],[0,1],[1,0],[0,-1]]
    dc=[[0,1],[1,0],[0,-1],[-1,0]]
    answer=0
    for k in range(4):
        drr=dr[k]
        dcc=dc[k]
        nm=0
        nm=space[r][c]
        cnt=0
        for l in range(2):
            nr=r+drr[l]
            nc=c+dcc[l]
            if -1<nr<n and -1<nc<m:
                nm+=space[nr][nc]
                cnt+=1
        if cnt==2:
            answer=max(answer,nm)
    return answer

def shape2(space,r,c):
    d=[[0,1],[1,0],[0,-1],[-1,0]]
    d2=[[0,2],[2,0],[0,-2],[-2,0]]
    answer=0
    for k in range(4):
        dr=d[k]
        dr2=d2[k]
        nm=0
        nm=space[r][c]
        cnt=0
        for l in range(2):
            nr=r+dr[l]
            nc=c+dr2[l]
            if -1<nr<n and -1<nc<m:
                nm+=space[nr][nc]
                cnt+=1
        if cnt==2:
            answer=max(answer,nm)
    return answer
answer=0
answer_value=0
for i in range(n):
    for j in range(m):
        ans_shape1=shape1(space,i,j)
        ans_shape2=shape2(space,i,j)
        answer=max(ans_shape1,ans_shape2)
        answer_value=max(answer,answer_value)
        
print(answer_value)