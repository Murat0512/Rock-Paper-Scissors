import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[^A-Za-z0-9]', password):
        return False
    return True

# Example usage
pwd = input("Enter your password: ")
if is_strong_password(pwd):
    print("Strong password!")
else:
    if not re.search(r'[A-Z]', pwd):
        print("You need at least 1 capital letters in your password.")
    elif not re.search(r'[^A-Za-z0-9]', pwd):
        print("You need at least 1special characters in your password.")
    else:
        print("Password is not strong enough.")