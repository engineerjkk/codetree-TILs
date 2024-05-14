import heapq
n=int(input())

for _ in range(n):
    m=int(input())
    lst=list(map(int,input().split()))
    pq=[]
    ans=[]
    heapleft=[]
    heapright=[]
    mid=[]
    for i in range(m): 
        if len(heapleft)==len(heapright):
            heapq.heappush(heapleft,-lst[i])
        else:
            heapq.heappush(heapright,lst[i])
        
        if heapright and -heapleft[0]>heapright[0]:
            big=heapq.heappop(heapleft)
            small=heapq.heappop(heapright)
            heapq.heappush(heapleft,-small)
            heapq.heappush(heapright,-big)
        if (i+1)%2==1:
            mid.append(-heapleft[0])
    for i in range(len(mid)):
        print(mid[i],end=" ")
    print()