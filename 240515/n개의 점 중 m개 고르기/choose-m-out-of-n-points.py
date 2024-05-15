from itertools import combinations

n,m=tuple(map(int,input().split()))
lst=[]
for _ in range(n):
    lst.append(list(map(int,input().split())))

nCr=combinations(lst,m)
ans=0

def dist(x1,x2,y1,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)
final_ans=1000000
for x in nCr:
    nXr=combinations(x,2)
    for j in nXr:
        distance=0
        distance=dist(j[0][0],j[1][0],j[0][1],j[1][1])
        ans=max(ans,distance)
    final_ans=min(final_ans,ans)
print(round(final_ans**2))