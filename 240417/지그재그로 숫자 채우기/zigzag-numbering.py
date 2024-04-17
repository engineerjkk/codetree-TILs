import sys
input = sys.stdin.readline

n,m = map(int,input().split())

space=[[0]*m for _ in range(n)]

count=0
for col in range(m):
    if col%2==0:
        for row in range(n):
            space[row][col]=count
            count+=1
    else:
        for row in range(n-1,-1,-1):
            space[row][col]=count
            count+=1

for row in range(n):
    for col in range(m):
        print(space[row][col],end=" ")
    print()