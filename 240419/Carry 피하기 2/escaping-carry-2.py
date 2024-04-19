import sys
input = sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    lst.append(int(input()))

ans=0
for i in range(n-2):
    arr_i=[0]*4 #0 0 0 0 0
    str_i=str(lst[i]) # 5 2 2
    m=-1
    for l in range(len(str_i)-1,-1,-1):
        arr_i[m]=str_i[l]
        m-=1
    ##############################
    for j in range(i+1,n-1):
        arr_j=[0]*4 #0 0 0 0 0
        str_j=str(lst[j]) # 5 2 2
        m=-1
        for l in range(len(str_j)-1,-1,-1):
            arr_j[m]=str_j[l]
            m-=1
        ##########################
        for k in range(j+1,n):
            arr_k=[0]*4 #0 0 0 0 0
            str_k=str(lst[k]) # 5 2 2
            m=-1
            for l in range(len(str_k)-1,-1,-1):
                arr_k[m]=str_k[l]
                m-=1
            cnt=0
            for p in range(len(arr_k)):
                if int(arr_i[p])+int(arr_j[p])+int(arr_k[p])<10:
                    cnt+=1
            if cnt==4:
                a = int(''.join(map(str, arr_i)))
                b = int(''.join(map(str, arr_j)))
                c = int(''.join(map(str, arr_k)))
                ans2=a+b+c
                ans=max(ans,ans2)

print(ans)