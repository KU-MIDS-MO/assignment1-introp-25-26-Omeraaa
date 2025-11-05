def sum_of_cubes_even(n):
    if not isinstance(n, int) or n < 0:
        return -1
    
    total = 0
    
    for i in range (0, n+1):
         if i % 2 == 0:
             total += i**3
        
    if n > 2000:
        print("warning")
    
    return(float(total))

print(sum_of_cubes_even(8))