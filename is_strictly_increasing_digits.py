def is_strictly_increasing_digits(n):
    if not isinstance(n, int) or n < 0:
        return -1
    
    s = str(n)
    prev = s[0]
    
    for ch in s[1:]:
        if ch <= prev:
            return False
        prev = ch
    
    return True

print(is_strictly_increasing_digits(1375))