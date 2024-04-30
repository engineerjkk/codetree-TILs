import sys
input = sys.stdin.readline
n,c,g,h = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
ans=0
tmp=0
for a in range(1001):
    tmp=0
    for i,j in lst:
        if a<i:
            tmp+=c
        elif i<=a<=j:
            tmp+=g
        else:
            tmp+=h
    ans=max(ans,tmp)
print(ans)