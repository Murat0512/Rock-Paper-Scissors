# Lists are 1 of 4 data colloections., holds multiple 
# values and we can reference tohse with common names 

users = ["Dave","John","Liz"]

# Can be any data 

data= ["Dave", 42, True]

# It can even be empty 

emptylist= []

#Always check if the list is empty or not 

print("Dave" in emptylist)

print("")

print(users[0])
print(users[-1])
print(users[-2])

# If we want a position of a specific value 

print(users.index("John"))

print(users[0:2])  # This does not include the 2nd value. ["Dave", "John"]

print(users[1:]) # This shows all the values till the end starting from 1

print(users[-3:-1])  # Accepts the negative numbers but it shows only 
# the existing values ["Dave", "John"]

print(len(data)) # 3 ( Dont confuse with index)

print("")

users.append ("Elsa")  # Adds values into the list ["Dave", "john", "Liz", "elsa"]
print(users)

users += ["Jason"]  # ['Dave', 'John', 'Liz', 'Elsa', 'Jason']
print(users)

users.extend(["Robert", "Kevin"])
#['Dave', 'John', 'Liz', 'Elsa', 'Jason', 'Robert', 'Kevin'
print(users)

# These method all added the items at the end of the list, we can
#also add the items at the end as well. 
print("")

users.insert(0, "Bob") # Insert command adds the item at the beginning 
print(users) # ['Bob', 'Dave', 'John', 'Liz', 'Elsa', 'Jason', 'Robert', 'Kevin']