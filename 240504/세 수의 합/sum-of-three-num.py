import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst=list(map(int,input().split()))

count={}
for elem in lst:
    if elem in count:
        count[elem]+=1
    else:
        count[elem]=1
ans=0
for i in range(n):
    count[lst[i]]-=1
    for j in range(i):
        diff = k - lst[i] - lst[j]
        if diff in count:
            ans+=count[diff]
print(ans)