def min_swaps_to_sort(arr):
    n = len(arr)
    
    # Create a list of tuples where each tuple is (index, element)
    indexed_arr = list(enumerate(arr))
    
    # Sort the array by the elements
    sorted_arr = sorted(indexed_arr, key=lambda x: x[1])
    
    # Create a visited array to mark visited elements
    visited = [False] * n
    
    swaps = 0
    
    for i in range(n):
        # If the element is already visited or it is already in the correct position
        if visited[i] or sorted_arr[i][0] == i:
            continue
        
        # Start a new cycle
        cycle_size = 0
        j = i
        
        while not visited[j]:
            visited[j] = True
            j = sorted_arr[j][0]  # Move to the next index in the cycle
            cycle_size += 1
        
        # If the cycle size is k, we need (k-1) swaps to sort it
        if cycle_size > 0:
            swaps += (cycle_size - 1)
    
    return swaps

# Example usage:
n = int(input())
weights = list(map(int, input().split()))

print(min_swaps_to_sort(weights))
