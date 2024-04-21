import sys
input = sys.stdin.readline
n,k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))
maximum=100
arr=[0]*(maximum+1)

for num,i in lst:
    arr[i]+=num

ans=0
answer=0
for i in range(maximum):
    nm=0
    for j in range(i-k,i+k+1):
        if -1<j<=maximum:
            nm+=arr[j]
    ans=max(ans,nm)
print(ans)