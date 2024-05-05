import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(str,input().strip())))

count={}
for i in lst:
    sorted_i=sorted(i)
    ans=""
    for j in sorted_i:
        ans+=j
    if ans in count:
        count[ans]+=1
    else:
        count[ans]=1
count2=sorted(count.items(),key=lambda x: x[1],reverse=True)
print(count2[0][1])
#문자열개수가 모두 맞는지 독립적으로 추가해줘서 and 조건을 맞추어줘야한다.