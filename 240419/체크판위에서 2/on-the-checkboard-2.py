import sys
input = sys.stdin.readline
r,c=map(int,input().split())

space=[]
for _ in range(r):
    space.append(list(map(str,input().split())))

cnt=0
for i in range(1,r-1):
    for j in range(1,c-1):
        for k in range(i+1,r-1):
            for l in range(j+1,c-1):
                if space[0][0]!=space[i][j] and space[i][j]!=space[k][l] and space[k][l]!=space[-1][-1]:
                    cnt+=1
print(cnt)