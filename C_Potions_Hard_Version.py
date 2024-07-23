import heapq

def fn(n, potions):
    current_health = 0
    min_heap = []
    num_potions = 0

    for potion in potions:
        if current_health + potion >= 0:
            
            current_health += potion
            heapq.heappush(min_heap, potion)
            num_potions += 1
        elif min_heap and min_heap[0] < potion:
            
            current_health += potion - heapq.heappop(min_heap)
            heapq.heappush(min_heap, potion)

    return num_potions

n = int(input())
potions = list(map(int, input().split()))
print(fn(n, potions))
