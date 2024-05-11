import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

tmp=sorted(lst,key=lambda x:(x[0],-x[1]))
ans=[]
for i in range(n):
    idx=lst.index(tmp[i])
    ans.append([tmp[i][0],tmp[i][1],idx+1])
for i in ans:
    for j in i:
        print(j,end=" ")
    print()