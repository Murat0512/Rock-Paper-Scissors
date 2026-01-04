def factorial_numbers(n):

    if n == 1:
        return 1 
    else:
        return n* (factorial_numbers(n-1))
    
print(factorial_numbers(5))