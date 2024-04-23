import sys
input=sys.stdin.readline
n,m= tuple(map(int,input().split()))

space=[list(map(int,input().split())) for _ in range(n)]


def get_num_of_gold(space,row,col,k):
    cnt=0
    for i in range(n):
        for j in range(n):
            if abs(i-row)+abs(j-col)<=k:
                cnt+=space[i][j]
    return cnt
    

answer=0
for row in range(n):
    for col in range(n):
        for k in range(n+1):
            if get_num_of_gold(space,row,col,k)*m >=(k*k+(k+1)*(k+1)):
                answer=max(answer,get_num_of_gold(space,row,col,k))
print(answer)