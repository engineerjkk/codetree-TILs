import sys
input = sys.stdin.readline
m1,d1,m2,d2=map(int,input().split())
A=str(input())
year=[31,29,31,30,31,30,31,31,30,31,30,31]
DayOfWeek=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

month=m1
day=d1
DoW=0
ans=0
if DayOfWeek[DoW]==A:
    ans+=1
while True:
    if month==m2 and day==d2:
        break
    day+=1
    DoW+=1
    if day>year[month-1]:
        day=1
        month+=1
    if DoW>6:
        DoW=0
    if DayOfWeek[DoW]==A:
        ans+=1
print(ans)