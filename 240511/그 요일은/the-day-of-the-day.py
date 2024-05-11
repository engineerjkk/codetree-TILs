m1, d1, m2, d2 = map(int,input().split())
day=str(input())

DoW=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
Month=[31,29,31,30,31,30,31,31,30,31,30,31]

cnt=0
ans=0
ans=0

d=d1
diff=0
for i in range(m1,m2+1):
    if i!=m2:
        for j in range(d,Month[i-1]+1):
            diff+=1
        d=1
    else:
        for j in range(d,d2+1):
            diff+=1
        d=1

for i in range(diff):
    if cnt>6:
        cnt=0
    today=DoW[cnt]
    if today == day:
        ans+=1
    cnt+=1

    last_month = Month[m1-1]
    d1+=1
    if d1>last_month:
        d1=1
        m1+=1
print(ans)