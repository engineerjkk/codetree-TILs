import sys
input = sys.stdin.readline
lst=list(map(str,input().strip()))


ans=0
cnt=0
for i in range(len(lst)-1,-1,-1):
    if lst[i]==")":
        cnt+=1
    else:
        ans+=cnt
print(ans)