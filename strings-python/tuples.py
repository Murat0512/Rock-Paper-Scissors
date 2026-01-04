# Tuples are immutable unlike lists, once they are created you cant modify tuples elements
# Tuples are more memory efficient
# Tuples have slightly higher time efficiency than lists
# They are in built data structures


# It is great if you have a sdata and dont need chenging in your code


my_tuple = (123, 456, 4578, 2334)


# Tuples can hold ona value as long as you as a coma after it, donet have to be a group of values

# Examnple: my_tuple= ("abc",)


print(my_tuple[0])  # prints abc

print(my_tuple[3:5])  # prints ( 456, True)

print(
    max(my_tuple)
)  # All the values have to be the same type like integer or all string

my_tuple1 = ("apple", " banana", "zebra", "zebra", "zebra")

print(max(my_tuple1))  # Zebra alphabetically at the end

# As max() , min() requires to have the same type of vlaues like integers and strings


print(my_tuple1.index("apple"))

print(
    my_tuple1.count("zebra")
)  # Counts how many times that item is repeated in a tuple
