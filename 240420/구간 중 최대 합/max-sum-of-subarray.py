import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst=list(map(int,input().split()))

ans=0

for i in range(n-k):
    summation=0
    for j in range(i,i+k):
        summation+=lst[j]
    ans=max(ans,summation)
print(ans)