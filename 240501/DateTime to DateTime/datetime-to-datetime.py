import sys
input = sys.stdin.readline
a,b,c=map(int,input().split())

day=11
hour=11
minute=11
ans=0
while True:
    if a<11 or (a<11 and b<11) or (a<11 and b<11 and c<11):
        print(-1)
        exit()
    if day==a and hour==b and minute==c:
        break
    ans+=1
    minute+=1
    if minute>60:
        minute=1
        hour+=1
    if hour>24:
        day+=1
        hour=1
print(ans)