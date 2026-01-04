numbers = [
    2,
    34,
    6,
    7,
    8,
    5,
    7,
    9,
    5,
]
print("The largest number is:", max(numbers))

print(
    "The number of occurrences of the largest number is:", numbers.count(max(numbers))
)

for num in set(numbers):
    print(f"The number {num} occurs {numbers.count(num)} times")
