import sys
input = sys.stdin.readline
n,k = map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(int(input()))

arr=[0]*n

ans=0
tmp=[]
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        else:
            if lst[i]==lst[j]:
                dis=abs(i-j)
                tmp.append(lst[i])
print(max(tmp))