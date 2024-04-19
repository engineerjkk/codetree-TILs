import sys
input = sys.stdin.readline

r,c=map(int,input().split())
space=[]
for _ in range(r):
    space.append(list(map(str,input().split())))

cnt=0
for i in range(r):
    for j in range(c):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if space[0][0] != space[i][j] and space[i][j] != space[k][l] and space[k][l] !=space[r-1][c-1]:
                    cnt+=1
print(cnt)