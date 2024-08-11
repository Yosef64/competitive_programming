def fn(s):  
    target = "hello"  
    target_index = 0  

    for char in s:  
        if char == target[target_index]:  
            target_index += 1  
        if target_index == len(target):  
            return "YES"  

    return "NO"  


s = input() 

result = fn(s)  
print(result)