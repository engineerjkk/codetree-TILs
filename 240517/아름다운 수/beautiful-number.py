import sys
input = sys.stdin.readline
from itertools import product
n = int(input())

lst=[]
for i in range(1,5):
    lst.append(i)

nCr=product(lst,repeat=n)

i=0
cnt=0
for x in nCr:
    check=True
    while i<n:
        check=True
        if i+x[i]-1>=n:
            check=False
        if check==True:
            for j in range(i,i+x[i]):
                if x[j]!=x[i]:
                    check=False
        i+=x[i]
        if check==True:
            cnt+=1
print(cnt)