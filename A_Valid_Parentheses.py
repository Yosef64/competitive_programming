def fn(s):
    stack = []
    ans = 0
    

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                ans += 1
            

    return ans*2
s = input()
print(fn(s))