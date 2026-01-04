# String Data types 
# Literal assignemt

first= "Dave"
last = "Gray"

# print(type(first))
# print(type(last))


# print(type(first) ==str)
# print(type(last) == str)

# print(type(first)==str)
# print(isinstance(first,str))

# Constructor fucntion 

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza)== str)
# print(isinstance(pizza,str))

# Concatenation 

# fullname = first + " " + last 

# print(fullname)
# fullname += "!"

# print(fullname)


# Casting a number to a string

# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = " I like rock music from the " + decade+ "'s"
# print(statement)

# #Multiple lines 

multiline= """Hey, How are you 

 I was just chacking in.             

                                 All good? 

 .....
 """

# print(multiline)

# # Escaping special characters 

# sentence=" I am back at work \t Hey!\n\n Where is this at\\located?"

# print(sentence)

# String Methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)


# print(multiline.title())
# print(multiline.replace("good","ok"))
# print(multiline)


# Original length of the multiline string shows with len 

# print(len(multiline))

# multiline += "                                                          "
# multiline = "                             " + multiline
# print(len(multiline))

# Removing white space from both side with strip , lstrip from the left and rstrip from the right

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


# # Build a menu  

# title = "menu". upper()
# print(title.center(20,"="))
# print ("Coffee". ljust(16,".") + "$1".rjust(4))
# print ("Muffin". ljust(16,".") + "$2".rjust(4))
# print ("C.Cake". ljust(16,".") + "$4".rjust(4))

# print("")

#String index

# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# Some methods return boolean value

print(first.startswith("D"))
print(first.endswith("Z"))

# Boolean data type 

myvalue = True
x= bool(False)
print(type(x))
print(isinstance(myvalue,bool))

# Numeric Data Types 

#Integer 

price = 100 
best_price = int(80)
print(type(price))
print(isinstance(best_price,int))

#Float Type 
print("")

gpa= 3.28
y= float(1.14)
print(type(gpa))


print("")

#complex type (j)

comp_value= 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print("")


# Built in functions or numbers 

print(abs(gpa)) # Absolute value

print(round(gpa))
print(round(gpa,1)) # rounds to the nearest decimal 3.28 to 3.3
print(abs(gpa*-1))


print("")

# Math module 

import math 

print(math.pi)

print(math.sqrt(64))

print(math.ceil(gpa))

print(math.floor(gpa))


print("")
# Casting a string to a number

zipcode = "10001" 
zip_value = int((zipcode))
print(type(zip_value))
print(zip_value)

# You can have an error if you attempt to cast incorrect data
#zipvalue = int("Newyork") # This will create an error in python 


