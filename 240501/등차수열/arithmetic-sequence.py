import sys
input = sys.stdin.readline
n = int(input())
lst=list(map(int,input().split()))
ans=0
for k in range(101):
    tmp=0
    for i in range(n):
        for j in range(i+1,n):
            if lst[j]-k == k-lst[i]:
                tmp+=1
    ans=max(ans,tmp)
print(ans)