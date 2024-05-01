import sys
input = sys.stdin.readline
import copy
n,m,k = map(int,input().split())
lst=[]
for _ in range(m):
    lst.append(int(input()))
tmp=[0]
for i in lst:
    tmp.append(i)
for i in range(k):
    for j,num in enumerate(lst):
        tmp[num]-=1
        if 0 in tmp[1:]:
            print(num)
            exit()


# 2,5,2,3,5,2,4
# 2,4,2,3,5,2,3
# 2,4,2,3,4,2,3
# 2,3,2,3,4,2,3
# 2,3,1,3,4,2,3
# 2,3,1,3,3,2,3
# 2,2,1,3,3,2,3
# 2,5,1,2,3,2,3
# 2,4,1,2,3,2,3
# 2,4,1,2,2,2,3
# 2,3,1,2,2,2,3
# 2,3,0,5