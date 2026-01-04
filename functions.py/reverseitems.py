def reversed_string(text):

    reversed_text= ""

    for char in text:
        reversed_text = char+reversed_text  # We force the first char to take the first place and pushed towards the end, 
        #then the second char comes and being pushed to the 2nd last position
    
    return reversed_text  # once all the chars pushed from first to last  ask to return the reversed_text

print(reversed_string("This is the string"))


