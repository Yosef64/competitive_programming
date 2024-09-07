def fn(n, s):
    stack = []
    mBra = [-1] * (2 * n)
    cCom = 0
    for i in range(2 * n):
        if s[i] == '(':
            stack.append(i)
        else:
            ind = stack.pop()
            mBra[i] = i
            if i - ind > 1:
                cCom += 1
    return cCom + 1

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    print(fn(n, s))