import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for i in range(n):
    lst.append(list(map(str,input().strip())))

count={}
a=ord('a')
for i in lst:
    cnt=0
    dic={}
    for j in i:
        if j in dic:
            dic[j]+=1
        else:
            dic[j]=1
    dic2=str(sorted(dic.items()))
    if dic2 in count:
        count[dic2]+=1
    else:
        count[dic2]=1
count2=sorted(count.items(),key=lambda x: x[1],reverse=True)
print(count2[0][1])
#문자열개수가 모두 맞는지 독립적으로 추가해줘서 and 조건을 맞추어줘야한다.