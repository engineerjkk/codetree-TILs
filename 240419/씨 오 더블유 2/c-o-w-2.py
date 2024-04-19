import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(str,input().strip()))

cnt=0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if lst[i]=="C" and lst[j]=="O" and lst[k]=="W":
                cnt+=1
print(cnt)