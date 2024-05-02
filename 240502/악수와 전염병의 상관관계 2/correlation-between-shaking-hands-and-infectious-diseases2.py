import sys
input = sys.stdin.readline
#n명의 개발자와 k번의 악수,개발자번호p, T개의 줄
n,k,p,T = map(int,input().split())

#리스트에는 t초에 x개발자와 y개발자가 악수를 나누었다.
lst=[]
for _ in range(T):
    lst.append(list(map(int,input().split())))

disease=[0]*(n+1)
move=[0]*(n+1)
disease[p]=1
sorted_lst=sorted(lst,key=lambda x : x[0])

cnt=0
start=False
for i in range(len(sorted_lst)):
    t,x,y=sorted_lst[i]
    if x ==p or y==p:
        start=True
    if start==True:
        if disease[x]>0 and move[x]<k and disease[y]==0:
            disease[y]+=1
            move[x]+=1
            cnt+=1
        elif disease[y]>0 and move[y]<k and disease[x]==0:
            disease[x]+=1
            move[y]+=1
            cnt+=1
        elif disease[x]>0 and disease[y]>0 and (move[x]<k or move[y]<k):
            move[x]+=1
            move[y]+=1

for i in range(1,n+1):
    if disease[i]>0:
        print(1,end='')
    else:
        print(0,end='')