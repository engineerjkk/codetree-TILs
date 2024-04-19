import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int,input().split()))

dis=1000000
for i in range(n):
    ans=0
    for j in range(n):
        ans+=lst[j]*abs(i-j)
    dis=min(dis,ans)
print(dis)