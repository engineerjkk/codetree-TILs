import sys
input = sys.stdin.readline
from itertools import combinations

n,b=map(int,input().split())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

students=0
for i in range(1,n+1):
    tmp=False
    nCr=combinations(lst,i)
    for j in nCr:
        # if i>4:
        #     print(j)
        price=[]
        deliver=[]
        for p,d in j: 
            price.append(p)
            deliver.append(d)
        sorted(price,reverse=True)
        price[0]=price[0]/2
        total=sum(price)+sum(deliver)
        if b>=total:
            stu=len(j)
            students=max(students,stu)
            tmp=True
            if tmp==True:
                continue
    if tmp==True:
        continue
print(students)