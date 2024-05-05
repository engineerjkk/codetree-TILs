import sys
input = sys.stdin.readline
n=int(input())
s=set()
ans=[]
for _ in range(n):
    lst=list(map(str,input().split()))
    order=lst[0]
    value=int(lst[1])
    if order=='find':
        if value in s:
            ans.append("true")
        else:
            ans.append("false")
    if order == 'add':
        s.add(value)
    if order == 'remove':
        s.remove(value)

for i in ans:
    print(i)