import sys
input = sys.stdin.readline
n,m =map(int,input().split())
lst_n=list(map(int,input().split()))
lst_m=list(map(int,input().split()))



dict_lst_n={}
for i in range(n):
    dict_lst_n[lst_n[i]]=0

for i in range(len(lst_n)):
    dict_lst_n[lst_n[i]]+=1

for i in range(len(lst_m)):
    if lst_m[i] in dict_lst_n:
        print(dict_lst_n[lst_m[i]],end=" ")
    else:
        print(0,end=" ")