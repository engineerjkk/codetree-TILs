import sys
input = sys.stdin.readline
x,y = map(int,input().split())
ans=0
for i in range(x,y+1):
    n=str(i)
    tmp=0
    for j in n:
        k=int(j)
        tmp+=k
    ans=max(ans,tmp)
print(ans)