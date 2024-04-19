import sys 
input = sys.stdin.readline
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))
value=0
visited=[[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n-2):
        cnt=space[i][j]+space[i][j+1]+space[i][j+2]
        if cnt>value:
            value=cnt
            coordinates=[[i,j],[i,j+1],[i,j+2]]

if coordinates:
    for i,j in coordinates:
        visited[i][j]=True

    second_value=0
    for i in range(n):
        for j in range(n-2):
            if not visited[i][j] and not visited[i][j+1] and not visited[i][j+2]:
                cnt=space[i][j]+space[i][j+1]+space[i][j+2]
                if cnt>second_value:
                    second_value=cnt
    print(value+second_value)
else:
    print(0)