import sys
input = sys.stdin.readline
n,h,t=map(int,input().split())
lst=list(map(int,input().split()))
ans=sys.maxsize
for i in range(n-t+1):
    value=0
    for j in range(i,i+t):
        value+=abs(h-lst[j])
    ans=min(ans,value)
print(ans)