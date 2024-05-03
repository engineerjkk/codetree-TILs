import sys
input = sys.stdin.readline
n = int(input())

d={}
ans=[]
for _ in range(n):
    total=list(map(str,input().split()))
    if len(total)==2:
        order, k = total[0], total[1]
        k=int(k)
    elif len(total)==3:
        order, k ,v = total[0], total[1], total[2]
        k=int(k)
        v=int(v)
    if order == 'add':
        d[k]=v
    elif order == 'find':
        if k in d:
            ans.append(d[k])
        else:
            ans.append("None")
    elif order == 'remove':
        d.pop(k)
for i in ans:
    print(i)