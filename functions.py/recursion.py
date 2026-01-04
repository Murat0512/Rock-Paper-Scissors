def factorial(num):
    call_stack = []
    if num ==1:
        print("Base case reached! Num is 1.")
        return 1
    else:
        call_stack.append({"input":num})
        print("Call Stack :" , call_stack)
        return num * factorial(num-1)
    
print(factorial(5))


def factorial(num):
    if num ==1: 
        return 1 
    else: 
        return num* factorial(num-1)
    
print(factorial(5))


