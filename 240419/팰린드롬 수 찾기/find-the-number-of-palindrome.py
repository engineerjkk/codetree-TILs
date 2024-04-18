import sys 
x,y = map(int,input().split())

cnt=0
for i in range(x,y+2):
    number=list(map(int,str(i).strip()))
    #print(number)
    for j in range(len(number)//2):
        if number[j]==number[-j-1]:
            cnt+=1
print(cnt)