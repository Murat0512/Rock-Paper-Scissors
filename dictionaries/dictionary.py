groceries= { "fruits": ["namgoes","apples", "bananas", "kiwis" ],
             "protein": ["beef", "pork", "chicken", "fish"],
             "carbs" : ["rice", "pasta", "bread"],
             "vegiies": ["lettuce", "cabbage", "onioons"] }

# Key -value pairs, 

# keys are inparanthesis, and values are in square brackets
# always seprate them with a coma if there is more than 1 key value

# It can contain lists, tuples, nesed dictionaries 
# BUT KEYS must always be immutable value  like STRING OR INTEGER OR TUPLE


party_planning = {'Yes': 10,
                  'No': 15,
                  'Maybe': 30,
                  'Location': 'Our Backyard',
                  'Date': '2022/05/01'}


print(party_planning["Date"])
print(party_planning["No"])
print(party_planning["Maybe"])
print(party_planning["Location"])
print(party_planning["Yes"])


print(len(party_planning))  # You can check the length of dictionary 

shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}

shopping_list1.update(shopping_list2)

print(shopping_list1)

print(shopping_list1.keys())
print(shopping_list1.values())  # You can print keys or vlaues of the dictionary using these 2 commands
