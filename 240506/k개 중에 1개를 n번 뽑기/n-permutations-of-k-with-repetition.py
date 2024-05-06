from itertools import combinations_with_replacement,permutations,combinations,product
k, n = map(int,input().split())

lst=[]
for i in range(1,k+1):
    lst.append(i)

nCr=product(lst,repeat=n)
for i in nCr:
    for j in i:
        print(j, end=" ")
    print()