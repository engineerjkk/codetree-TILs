import sys
input = sys.stdin.readline
m1,d1,m2,d2 = map(int,input().split())

month=m1
day=d1
DoW=1
DayOfWeek=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
year=[31,28,31,30,31,30,31,31,30,31,30,31]
while True:
    if month==m2 and day==d2:
        print(DayOfWeek[DoW])
        exit()
    if month==12 and day==31:
        break
    day+=1
    if day>year[month-1]:
        day=1
        month+=1
    DoW+=1
    if DoW>6:
        DoW=0
while True:
    if month==1 and day==1:
        break
    if month==m2 and day==d2:
        print(DayOfWeek[DoW])
        exit()
    day-=1
    if day<1:
        month-=1
        day=year[month-1]
    DoW-=1
    if DoW<0:
        DoW=6