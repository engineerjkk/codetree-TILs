# import sys
# input = sys.stdin.readline
n,k = tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(int(input()))

ans=0
for i in range(n-1):
    for j in range(i+1,n):
        # if i==j:
        #     continue
        if lst[i]==lst[j]:
            if lst[i]>=abs(i-j):
                ans=max(ans,lst[i])
print(ans)