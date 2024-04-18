import sys 
x,y = map(int,input().split())

ans=0
for i in range(x,y+1):
    number=list(str(i).strip())
    #print(number)
    cnt=0
    for j in range(len(number)//2):
        if number[j]==number[-j-1]:
            cnt+=1
    if cnt==len(number)//2:
        ans+=1
        
print(ans)