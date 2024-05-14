import heapq

n=int(input())
lst=list(map(int,input().split()))

sum_avg=0
ans=0

sum_avg+=lst[n-1]
pq=[]

for i in range(n-2,0,-1):
    heapq.heappush(pq,lst[i])
    sum_avg+=lst[i]
    min_value=pq[0]
    avg=(sum_avg-min_value)/(n-i-1)

    ans=max(ans,avg)
print(f"{ans:.2f}")