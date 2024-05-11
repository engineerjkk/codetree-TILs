import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

tmp=sorted(lst,key=lambda x:(x[0],-x[1]))
for i in range(n):
    tmp[i].append(i+1)
for i in tmp:
    for j in i:
        print(j,end=" ")
    print()