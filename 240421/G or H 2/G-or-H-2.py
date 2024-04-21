import sys
input = sys.stdin.readline

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(str,input().split())))

lst.sort(key=lambda x: int(x[0]))
ans=0
for i in range(n):
    for j in range(i,n):
        space=[]
        for k in range(i,j):
            space.append(lst[k])
        tmp_num=[]
        tmp_cha=[]
        for num,cha in space:
            tmp_num.append(int(num))
            tmp_cha.append(cha)

        if len(tmp_num)>=2:
            if len(list(set(tmp_cha)))==1 or tmp_cha.count("G")==tmp_cha.count("H"):
                ans=max(ans,max(tmp_num)-min(tmp_num))
print(ans)