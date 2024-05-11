import sys
input = sys.stdin.readline
n = int(input())
lst=list(map(int,input().split()))
ans=-sys.maxsize
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if i==j or i==k or j==k:
                continue
            else:
                value=lst[i]*lst[j]*lst[k]
            ans=max(ans,value)
print(ans)