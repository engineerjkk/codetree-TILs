import sys
input = sys.stdin.readline
a,b,c,d=map(int,input().split())

hour=a
minute=b
ans=0
while True:
    if hour==c and minute==d:
        break
    minute+=1
    ans+=1
    if minute==60:
        minute=0
        hour+=1
print(ans)