import sys
input = sys.stdin.readline
from itertools import combinations

n,b=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))


students=0
for i in range(1,n+1):
    nCr=combinations(lst,i)

    for j in nCr:
        price=[]
        deliver=[]
        for p,d in j: 
            price.append(p)
            deliver.append(d)
        #print(len(price))
        a=price.index(max(price))
        price[a]=price[a]/2
        total=sum(price)+sum(deliver)
        if b>=total:
            stu=len(price)
            students=max(students,stu)
print(students)