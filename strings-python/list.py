list = [ "abc", 123, "def" , 10.5 , [ 1,3,6]]

print(list[4])
print(list)
print(list[2])
print(list[2:5])
print(len(list))


list.append("Murat")  # Added Murat at the end of  the list 

print(list)

list.remove(10.5) # removed the item from the list

print(list)


list.pop ()  # removes the last item 

print(list)

list.pop(0)  # removes the item given in the pop paranthesis

print(list)