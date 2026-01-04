def even_nums(nums):

    count= 0 
    for num in nums: 
        if num % 2 == 0:
            count +=num 
    return count


print(even_nums([2,4,6,3,5,7,24]))