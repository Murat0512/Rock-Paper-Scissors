nums= {1,2,3,4} # Normal creating set 

num2 = set((1,2,3,4))  # Constructor method 

print(nums)
print(num2)
print(type(nums))
print(type(num2))

print(len(nums))

# No duplicates allowed

nums = {1,2,2,3,4}

print(nums) # prints 1,2,3,4


nums = {1,True,False,2,3,4,5}

print(nums) #  {False, 1, 2, 3, 4, 5} False means zero it put in the front

print(2 in nums)

# You can not refer to an element in a set with an index position or a key 


# Add an element to a set 

nums.add(8)

print(nums)


# Add elements from one set to another 


morenums= {5,6,7,8,9}

nums.update(morenums)

print(nums)

# you can use update() lists, tuples, dictionaries

#Merge 2 sets to create a new set 

one ={1,2,3,5}
two= {7,9,8,6}

mynewset= one.union(two)

print(mynewset)

# Keep  only duplicates t 

one ={1,2,3,5}
two= {2,3,5,7}

one.intersection_update(two)

print(one)# {2, 3, 5}


#We are going to keep the numbers except the duplicates 

one ={1,2,3,5}
two= {2,3,5,7}

one.symmetric_difference_update(two)

print(one)# prints{1, 7}