import sys
input = sys.stdin.readline
from itertools import product
n=int(input())

lst=[]
for i in range(1,5):
    lst.append(i)

nCr=product(lst,repeat=n)
cnt=0
tmp=[]
for x in nCr:
    check=True
    i=0
    check=True
    while i<n:
        if i+x[i]-1>=n:
            check=False
        if check==True:
            for j in range(i,i+x[i]):
                if x[j] !=x[i]:
                    check=False
        i +=x[i]
    if check==True:
        cnt+=1
print(cnt)