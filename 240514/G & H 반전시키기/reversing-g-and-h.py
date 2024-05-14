n=int(input())
start=input()
end=input()

cnt=0
mismatched=True

for i in range(n):
    if start[i]!=end[i] and mismatched==True :
        mismatched=False
        cnt+=1
    else:
        mismatched=True
print(cnt)