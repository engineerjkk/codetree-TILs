import sys
input = sys.stdin.readline
n= int(input())
lst_n=list(map(int,input().split()))
m = int(input())
lst_m=list(map(int,input().split()))


set_n=set(lst_n)
#set_m=set(lst_m)
for i in lst_m:
    if i in set_n:
        print(1,end=" ")
    else:
        print(0,end=" ")