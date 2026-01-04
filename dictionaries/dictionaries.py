#Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
    
    }

band2= dict(vocals= "Plant", guitar= "Page") # Constructor method

print(band)
print(band2)

print(type(band))  # you can print type of a dictionary 
print(len(band)) # you can get a length of a dictionary


#Access items in a dictionary 

print(band["vocals"])

print(band.get("guitar"))

#list all the keys 

print(band.keys())


#list all vlaues 

print(band.values())

# list of key/value pairs as tuples

print(band.items())


#Verify if key exists 

print("guitar" in band)
print("triangle" in band)


# Change vlaues

band["vocals"]= "Coverdale"

print(band)

band.update({"base": "JPJ"})

print(band)


#Remove items 

print(band.pop("base"))

print(band)


band["drums"] = "bonham"

print(band.popitem())

print(band)


#delete and clear 


band ["drums"] = "Bonham"

print(band)

del band["drums"] 

print(band)

band2.clear 

print(band2)