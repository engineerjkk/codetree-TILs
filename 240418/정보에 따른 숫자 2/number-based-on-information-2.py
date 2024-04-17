import sys 
input = sys.stdin.readline


def count_nearest_type(T,a,b):
    
    N=[]
    S=[]
    for _ in range(T):
        alpha,num = map(str,input().split())
        if alpha=='N':
            N.append(int(num))
        elif alpha=='S':
            S.append(int(num))
        
    N.sort()
    S.sort()
    s_idx,n_idx,cnt=0,0,0
    for i in range(a,b+1):
        while s_idx<len(S)-1 and abs(i-S[s_idx])>abs(i-S[s_idx+1]):
            s_idx+=1
        ds=abs(i-S[s_idx])

        while n_idx<len(N)-1 and abs(i-N[n_idx])>abs(i-N[n_idx+1]):
            n_idx+=1
        dn=abs(i-N[n_idx])

        if ds<=dn:
            cnt+=1
    return cnt




T,a,b=list(map(int,input().split()))
print(count_nearest_type(T,a,b))