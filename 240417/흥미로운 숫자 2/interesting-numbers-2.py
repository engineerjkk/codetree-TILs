import sys
input = sys.stdin.readline
x,y=map(int,input().split())

count=0
for i in range(x,y+1):
    lst=list(map(int,list(str(i))))
    unique=list(set(lst))
    value={}
    for j in unique:
        value[j]=0
    for j,num in enumerate(lst):
        value[num]+=1
    if len(unique)==2:
        for key,val in value.items():
            if val==1:
                count+=1
print(count)