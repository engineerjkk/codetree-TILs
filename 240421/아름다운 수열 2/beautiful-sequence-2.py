import sys
input = sys.stdin.readline
n,m = map(int,input().split())
n_lst=list(map(int,input().split()))
m_lst=list(map(int,input().split()))

cnt=0
for i in range(0,n-m+1):
    if sorted(n_lst[i:i+m])==sorted(m_lst):
        cnt+=1

print(cnt)