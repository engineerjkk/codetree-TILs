import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))
ans=0
for i in range(1001):
    tmp=0
    arr=[False]*n
    for j in range(n):
        if lst[j]>i:
            arr[j]=True
    tmpp=False
    for j in range(n):
        if arr[j]==True and tmpp==False:
            tmp+=1
            tmpp=True
        elif arr[j]==False:
            tmpp=False
    ans=max(ans,tmp)
print(ans)