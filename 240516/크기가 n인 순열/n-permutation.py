from itertools import permutations
n=int(input())
lst=[]
for i in range(1,n+1):
    lst.append(i)

nCr=permutations(lst,n)
ans=[]
for x in nCr:
    for i in x:
        print(i,end=" ")
    print()