import sys
input = sys.stdin.readline
n,m = map(int,input().split())
space=[]
for _ in range(n):
    space.append(list(map(str,input().split())))


cnt=0
for i in range(1,n):
    for j in range(1,m):
        for k in range(i+1,n-1):
            for l in range(j+1,m-1):
                if space[0][0] != space[i][j] and space[i][j] != space[k][l] and space[k][l]!=space[n-1][m-1]:
                    cnt+=1
print(cnt)