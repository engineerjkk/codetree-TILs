from itertools import combinations
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst=[]
for i in range(1,n+1):
    lst.append(i)

nCr=combinations(lst,m)
for x in nCr:
    for i in x:
        print(i,end=" ")
    print()