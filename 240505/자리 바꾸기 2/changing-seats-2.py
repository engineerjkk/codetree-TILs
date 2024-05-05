import sys
input = sys.stdin.readline
n,k = tuple(map(int,input().split()))
lst=[]
for _ in range(k):
    lst.append(list(map(int,input().split())))

s=[]
for i in range(n+1):
    s.append(set())

seat=[]
for i in range(n+1):
    seat.append(i)
ans=[]
for i in range(n+1):
    ans.append(1)

for i in range(1,n+1):
    s[i].add(i)

for _ in range(3):
    for (a,b) in lst:
        seat[a],seat[b]=seat[b],seat[a]

        if a not in s[seat[a]]:
            s[seat[a]].add(a)
            ans[seat[a]]+=1
        if b not in s[seat[b]]:
            s[seat[b]].add(b)
            ans[seat[b]]+=1
for i in range(1,n+1):
    print(ans[i])