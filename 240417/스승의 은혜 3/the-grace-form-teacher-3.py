import sys
input = sys.stdin.readline
from itertools import combinations

n,b=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))


students=0
for i in range(2,n+1):
    tmp=False
    nCr=combinations(lst,i)

    for j in nCr:
        price=[]
        deliver=[]
        # print("___")
        # print(j)
        for p,d in j: 
            price.append(int(p))
            deliver.append(int(d))
            #print(len(price))
        a=price.index(max(price))
        price[a]=int(price[a]/2)
        total=sum(price)+sum(deliver)
        if b>=total:
            stu=len(price)
            students=max(students,stu)
print(students)