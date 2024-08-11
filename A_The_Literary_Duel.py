def solve_game(n, books):
    hermione_score = 0
    harry_score = 0
    turn = 0 
    
    left = 0
    right = n - 1
    
    while left <= right:
        if books[left] >= books[right]:
            chosen_book = books[left]
            left += 1
        else:
            chosen_book = books[right]
            right -= 1
        
        if turn == 0:
            hermione_score += chosen_book
        else:
            harry_score += chosen_book
        turn = 1 - turn
    
    return hermione_score, harry_score


n = int(input())
books = list(map(int, input().split()))

hermione_score, harry_score = solve_game(n, books)

print(hermione_score, harry_score)
