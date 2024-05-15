import sys
input = sys.stdin.readline
import heapq
n=int(input())
lst=[]
pq=[]
for _ in range(n):
    a = int(input())
    if a!=0:
        heapq.heappush(pq,(abs(a),a))
    else:
        if pq:
            b=heapq.heappop(pq)
            lst.append(b[1])
        else:
            lst.append(0)
for i in lst:
    print(i)