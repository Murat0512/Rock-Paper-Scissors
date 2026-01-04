text= "Hello world. How are you,I need myvovels counted"

vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)