def reverse_string(s):
    reversed_str = ""
    i = len(s) - 1
    while i >= 0:
        reversed_str += s[i]
        i -= 1
    return reversed_str

# Example usage
input_str = "hello"
print(reverse_string(input_str))  # Output: "olleh"