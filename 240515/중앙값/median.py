import sys
import heapq
input = sys.stdin.readline
n=int(input())

for _ in range(n):
    m=int(input())
    lst=list(map(int,input().split()))
    max_heap=[]
    min_heap=[]
    mid=[]
    for j in range(m):
        if len(max_heap)==len(min_heap):
            heapq.heappush(max_heap,-lst[j])
        else:
            heapq.heappush(min_heap,lst[j])
        
        if min_heap and -max_heap[0]>min_heap[0]:
            big = -heapq.heappop(max_heap)
            small = heapq.heappop(min_heap)
            heapq.heappush(min_heap,big)
            heapq.heappush(max_heap,-small)
        if (j+1)%2==1:
            mid.append(-max_heap[0])
    for j in range(len(mid)):
        print(mid[j],end=" ")
    print()