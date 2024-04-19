import sys 
input = sys.stdin.readline
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
value=0
visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(1,n-1):
        cnt=space[i][j-1]+space[i][j]+space[i][j+1]
        if cnt>value:
            value=cnt
            coordinates=[[i,j-1],[i,j],[i,j+1]]

for i,j in coordinates:
    visited[i][j]=True

second_value=0
for i in range(n):
    for j in range(1,n-1):
        if not visited[i][j-1] and not visited[i][j] and not visited[i][j+1]:
            cnt=space[i][j-1]+space[i][j]+space[i][j+1]
            if cnt>second_value:
                second_value=cnt
print(value+second_value)