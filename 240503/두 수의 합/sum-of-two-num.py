import sys
input = sys.stdin.readline
n,k=map(int,input().split())
arr=list(map(int,input().split()))
dic={}
ans=0
for i in arr:
    diff = k - i
    if diff in dic:
        ans+=dic[diff]
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(ans)