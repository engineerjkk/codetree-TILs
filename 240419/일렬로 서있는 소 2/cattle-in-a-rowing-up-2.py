import sys 
input = sys.stdin.readline

n=int(input())
lst=list(map(int,input().split()))

cnt=0
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            if lst[i]<=lst[j] and lst[j]<=lst[k] and lst[i]<=lst[k]:
                cnt+=1
print(cnt)