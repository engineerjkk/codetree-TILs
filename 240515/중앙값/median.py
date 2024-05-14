import heapq
n=int(input())

for _ in range(n):
    m=int(input())
    lst=list(map(int,input().split()))
    pq=[]
    ans=[]
    heapmax=[]
    heapmin=[]
    mid=[]
    for i in range(m): 
        if len(heapmax)==len(heapmin):
            heapq.heappush(heapmax,-lst[i])
        else:
            heapq.heappush(heapmin,lst[i])
        
        if heapmin and -heapmax[0]>heapmin[0]:
            big=-heapq.heappop(heapmax)
            small=heapq.heappop(heapmin)
            heapq.heappush(heapmax,-small)
            heapq.heappush(heapmin,big)
        if (i+1)%2==1:
            mid.append(-heapmax[0])
    for i in range(len(mid)):
        print(mid[i],end=" ")
    print()