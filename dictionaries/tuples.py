# Tuples are similar to lists but you cant change the order and conten (data) inside the tuple.
firsttuple= tuple(("Dave", 42, "Kevin", True))


another_tuple = (1,3,5,7,89)

# lets unpack the above tuple 

(one, *two, hey) = another_tuple

print(one) # prints 1 
print(two) # prints 3,5,7
print(hey) # prints 89 Wherever you put the * it makes the remianing values a list including that value

print(tuple)
print(type(tuple))


print(another_tuple)
print(type(another_tuple))


# Since we can not modify tuples we can use list to add new values by creating a 
#new list from the exisiting tuple and reverting the list back to tuple later on 
mylist= list(firsttuple)

mylist.append("Neil")
newtuple= tuple(mylist)
print(newtuple)



