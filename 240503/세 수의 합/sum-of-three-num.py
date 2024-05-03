import sys
input = sys.stdin.readline
n, k = map(int,input().split())
lst=list(map(int,input().split()))
dic={}
ans=0

for i in range(n-1):
    for j in range(i+1,n):
        if i==j:
            continue
        else:
            value = lst[i]+lst[j]
            diff = k - lst[i] - lst[j]
            if diff in dic:
                ans+=dic[diff]
            if value in dic:
                dic[value]+=1
            else:
                dic[value]=1
print(ans)