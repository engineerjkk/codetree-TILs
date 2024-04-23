import sys
input = sys.stdin.readline
n = int(input())

lines=[]
mil=1000000
check=[0]*(mil*2+1)
for _ in range(n):
    a=list(map(int,input().split()))
    a.sort
    lines.append(a)



lines.sort(key=lambda x:x[0])

def check_point(start,end):
    for i in range(start,end):
        check[i]+=1

    for i in range(start,end):
        if check[i]>=2:
            return False
    return True

def mask(start,end):
    for i in range(start,end):
        check[i]=1
    return 1

ans=0
for i in range(n):
    start,end=lines[i]
    start=start+mil
    end=end+mil
    if check_point(start,end+1):
        ans+=mask(start,end+1)
print(ans)