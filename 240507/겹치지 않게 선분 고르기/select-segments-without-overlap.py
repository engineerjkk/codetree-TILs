import sys
input = sys.stdin.readline
from itertools import combinations

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

lst=sorted(lst)
MAX=1001


comb=[]
for i in range(n):
    comb.append(i)

for i in range(n,0,-1):
    nCr=combinations(comb,i)
    check=False
    for x in nCr:
        arr=[0]*MAX
        #print(x)
        for k in x:
            start=lst[k][0]
            end=lst[k][1]
            for j in range(start,end+1):
                arr[j]+=1
        if arr.count(0)+arr.count(1)==len(arr):
            check=True
        if check==True:
            print(i)
            exit()