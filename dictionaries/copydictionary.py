band = {
    "vocals": "Plant",
    "guitar": "Page"
    
    }

# band2= band # Creates a reference, they are not the
#same they just refers to same memory
#BAD COPY
# print(band2)
# print(band)

# band2["drums"] = "Dave"

# print(band2)
# print(band)

band2= band.copy() # This creates a copy of the band , 
#if you dont create a copy it will change band, change you make in 
# band2 wuill be affecting band as well.


band2["bass"]= "Dave" 
print("Good Copy")
print(band2)
print(band)


band3= dict(band)

print(band3)


