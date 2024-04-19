import sys
import copy
input = sys.stdin.readline
MAX=sys.maxsize
n=int(input())
space=[]

for _ in range(n):
    space.append(list(map(int,input().split())))
NumPoints=len(space)
dis=MAX

def cal(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

for i in range(NumPoints):
    space2=copy.deepcopy(space)
    if 0<i<NumPoints-1:
        distance=0
        del space2[i]
        for j in range(len(space2)-1):
            x1,y1=space2[j]
            x2,y2=space2[j+1]
            distance+=cal(x1,y1,x2,y2)
        dis=min(dis,distance)
print(dis)