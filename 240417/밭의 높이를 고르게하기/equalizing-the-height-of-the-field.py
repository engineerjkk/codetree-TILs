import sys
input = sys.stdin.readline
n,h,t =map(int,input().split())
lst=list(map(int,input().split()))


total_cnt=100*100
for i in range(n-t+1):
    cnt=0
    for j in range(i,i+t):
        cnt+=abs(t-lst[j])
    total_cnt=min(total_cnt,cnt)

print(total_cnt)