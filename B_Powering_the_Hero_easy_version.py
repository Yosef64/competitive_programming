import heapq


test= int(input())
for _ in range(test):
    n = int(input())
    arr = list(map(int,input().split()))
    heap = []
    ans = 0
    for card in arr:
        if card == 0:
            if heap:
                ans -= heapq.heappop(heap)
        else:
            heapq.heappush(heap,-card)
    print(ans)