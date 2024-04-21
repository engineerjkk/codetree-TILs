import sys
input = sys.stdin.readline
n=int(input())
space=[]
for _ in range(n):
    space.append(list(map(int,input().split())))

ans=0
for i in range(n-3+1):
    for j in range(n-3+1):
        nm=0
        for k in range(i,i+3):
            for l in range(j,j+3):
                nm+=space[k][l]
        ans=max(nm,ans)
print(ans)