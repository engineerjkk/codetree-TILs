import sys
input = sys.stdin.readline
import copy
n= int(input())
lst=list(map(str,input().split()))

cnt=0
tmp=copy.deepcopy(lst)
tmp.sort()
while lst!=tmp:
    for i in range(n-1):
        if ord(lst[i])>ord(lst[i+1]):
            lst[i],lst[i+1]=lst[i+1],lst[i]
            cnt+=1
print(cnt)