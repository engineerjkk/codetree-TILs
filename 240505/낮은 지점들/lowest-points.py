import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

dic={}
for i in range(n):
    x,y=lst[i]
    if x in dic:
        dic[x].append(y)
    else:
        dic[x]=[y]
ans=0
for key,value in dic.items():
    sorted_value=sorted(value)
    ans+=sorted_value[0]
print(ans)