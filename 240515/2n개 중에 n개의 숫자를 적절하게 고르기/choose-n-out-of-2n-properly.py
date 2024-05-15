import sys
from itertools import combinations
n= int(input())
lst=list(map(int,input().split()))
lst.sort()
nCr=combinations(lst,len(lst)//2)

arr=[]
for x in nCr:
    arr.append(x)
dictionary={}
for i in range(len(arr)//2):
    dictionary[arr[i]]=arr[len(arr)-i-1]

ans=100000000
for key,value in dictionary.items():
    ans2=abs(sum(key)-sum(value))
    ans=min(ans,ans2)
print(ans)