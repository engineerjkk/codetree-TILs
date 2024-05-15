import sys
from itertools import combinations
n= int(input())
lst=list(map(int,input().split()))
lst.sort()
nCr=combinations(lst,len(lst)//2)

lst_a=[]
lst_b=[]
for i in range(n):
    if i%2==0:
        lst_a.append(lst[i])
        lst_a.append(lst[2*n-i-1])
    else:
        lst_b.append(lst[i])
        lst_b.append(lst[2*n-i-1])
print(abs(sum(lst_a)-sum(lst_b)))