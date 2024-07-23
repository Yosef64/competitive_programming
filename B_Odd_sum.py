n = int(input())
array = list(map(int,input().split()))
minNeg , posSum ,minPos = float("-inf"), 0, float("inf")

for num in array:
    if num < 0 and abs(num)%2:
        minNeg = max(minNeg,num)
    elif num >0:
        if num % 2:
            minPos = min(minPos,num)
        posSum += num
if posSum % 2:
    print(posSum)
else:
    print(max(posSum + minNeg,posSum - minPos))
    