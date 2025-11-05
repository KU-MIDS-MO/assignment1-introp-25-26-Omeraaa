def count_digits_greater_than(n, t):
    if not isinstance(n, int) or not isinstance(t, int) or n < 0:
        return -1
    
    if t < 0 or t > 9:
        return -1
    
    s = str(n)
    count = 0
    
    for ch in s:
        if int(ch) > t:
            count +=1
            
    return count

print(count_digits_greater_than(3579, 2))