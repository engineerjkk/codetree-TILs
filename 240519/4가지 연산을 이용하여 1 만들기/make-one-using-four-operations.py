import sys
input = sys.stdin.readline
from collections import deque
from itertools import product

n = int(input())
cal=[0,1,2]

def plus(value):
    return value+1
def minus(value):
    return value-1

def divide(value):
    if value%2==0:
        return value//2
    elif value%3==0:
        return value//3

queue=deque()
queue.append(n)

for i in range(n):
    nCr=product(cal,repeat=i)
    for x in nCr:
        value=n
        for j in x:
            check=True
            if j==0:
                value=plus(value)
            elif j==1:
                value=minus(value)
            else:
                if value%3!=0 and value%2!=0:
                    check=False
                else:
                    value=divide(value)
            if check==False:
                break
            if value==1:
                print(i)
                exit()
print(0)