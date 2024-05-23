import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst=list(map(int,input().split()))


def find(target):
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if lst[mid]==target:
            return mid
        if lst[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

for _ in range(m):
    tar=int(input())
    ans=find(tar)
    if ans<0:
        print(-1)
    else:
        print(ans+1)