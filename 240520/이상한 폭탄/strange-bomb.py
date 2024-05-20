import sys
input = sys.stdin.readline
n, k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))

R=[0]*n
latest_index=dict()
for i in range(n-1,-1,-1):
    if lst[i] not in latest_index:
        R[i]=-1
    else:
        R[i]=latest_index[lst[i]]
    latest_index[lst[i]]=i

ans=-1
for i in range(n):
    if R[i] !=-1 and i-R[i]<k:
        ans=max(ans,lst[i])
print(ans)