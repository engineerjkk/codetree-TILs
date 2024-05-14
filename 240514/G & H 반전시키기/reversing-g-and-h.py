n=int(input())
start=input()
end=input()

cnt=0
mismatched=False

for i in range(n):
    if start[i]!=end[i] and mismatched==False :
        mismatched=True
        cnt+=1
    else:
        mismatched=False
print(cnt)