import sys
input = sys.stdin.readline
a,b = map(int,input().split())
lst_a=list(map(int,input().split()))
lst_b=list(map(int,input().split()))

set_a=set()
set_b=set()
for i in range(a):
    set_a.add(lst_a[i])

for i in range(b):
    set_b.add(lst_b[i])

ans=set()
for i in set_b:
    if i not in set_a:
        ans.add(i)

for i in set_a:
    if i not in set_b:
        ans.add(i)

print(len(ans))