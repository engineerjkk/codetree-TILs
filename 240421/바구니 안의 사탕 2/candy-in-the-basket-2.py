import sys
input = sys.stdin.readline
n,k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
arr=[0]*101

for num,i in lst:
    arr[i]+=num

ans=0
answer=0
for i in range(k,101-k+1):
    nm=0
    for j in range(i-k,i+k+1):
        nm+=arr[j]
    if nm>ans:
        ans=nm
        answer=i
print(ans)