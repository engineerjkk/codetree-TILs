import sys
input = sys.stdin.readline
n,m = map(int,input().split())

space=[i for i in range(n*m)]

for i in range(n):
    print(space[i],end=" ")
    print(space[-i-1])