import sys
input = sys.stdin.readline
n, t = map(int,input().split())
lst=list(map(int,input().split()))

ans=0
for i in range(n):
    for j in range(n):
        arr=[]
        cnt=0
        for k in range(i,j+1):
            if lst[k]>t:
                cnt+=1
        if cnt==(j-i+1):
            ans=max(ans,cnt)
print(ans)