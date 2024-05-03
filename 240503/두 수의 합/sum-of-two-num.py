import sys
input = sys.stdin.readline
n, k = map(int,input().split())
dic={}
lst=list(map(int,input().split()))
ans=0
for i in range(n):
    dic[i]=lst[i]
for i in range(n-1):
    for j in range(i+1,n):
        if dic[i]+dic[j]==k:
            ans+=1
print(ans)