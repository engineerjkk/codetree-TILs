import sys
input = sys.stdin.readline
from itertools import combinations

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

sorted(lst)
MAX=1001
arr=[0]*MAX

comb=[]
for i in range(n):
    comb.append(i)

for i in range(n,0,-1):
    nCr=combinations(comb,i)
    check=True
    for x in nCr:
        for k in x:
            start=lst[k][0]
            end=lst[k][1]
            for j in range(start,end+1):
                arr[j]+=1
                if arr[j]>=2:
                    check=False
                    break
            if check==False:
                break
            else:
                print(i)
                exit()