import sys
input = sys.stdin.readline
from itertools import product
n=int(input())

lst=[]
for i in range(1,n+1):
    lst.append(i)

nCr=product(lst,repeat=n)
cnt=0
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


    #     if x[i]==1:
    #         i+=1
    #     elif x[i]==2:
    #         if n<i+2:
    #             check=False
    #         for j in range(i,i+2):
    #             if x[i] !=2:
    #                 check=False
    #                 break
    #         i+=(j-i+1)
    #     elif x[i]==3:
    #         if n<i+3:
    #             check=False
    #         for j in range(i,i+3):
    #             if x[i] !=3:
    #                 check=False
    #                 break
    #         i+=(j-i+1)
    #     elif x[i]==4:
    #         if n<i+4:
    #             check=False
    #         for j in range(i,i+4):
    #             if x[i] !=4:
    #                 check=False
    #                 break
    #         i+=(j-i+1)
    # if check==True:
    #     print(x)
    #     cnt+=1