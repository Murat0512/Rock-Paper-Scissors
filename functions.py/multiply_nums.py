def multiply_nums(nums):

    multiply = 1 # Because it is multiplication multiply can not take the value of 0 otherwise everything will be multiplied by 0 
    for num in nums: 
        multiply *=num

    return multiply


print(multiply_nums([1,2,4,6]))