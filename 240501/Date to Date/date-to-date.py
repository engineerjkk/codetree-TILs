import sys
input = sys.stdin.readline
m1,d1,m2,d2 = map(int,input().split())

year=[31,28,31,30,31,30,31,31,30,31,30,31]

month=m1
day=d1
ans=0
while True:
    if month==m2 and day==d2:
        break
    ans+=1
    day+=1
    if day==year[month-1]:
        month+=1
        day=1
print(ans+2)