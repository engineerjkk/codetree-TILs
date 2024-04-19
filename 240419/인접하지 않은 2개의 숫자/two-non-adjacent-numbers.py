import sys
input = sys.stdin.readline
INT_MIN= -sys.maxsize
n=int(input())
lst=list(map(int,input().split()))

num=INT_MIN
for i in range(n-1):
    for j in range(i+1,n):
        if abs(i-j)>1:
            ans=lst[i]+lst[j]
            num=max(num,ans)
print(num)