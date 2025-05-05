# 🔹 Problem 1: Reverse a String
# Write a function that takes a string as input and returns the reversed string.
# Example:
# 🔹 Input: "hello"
# 🔹 Output: "olleh"
# 💡 Hint: Use Python's slicing feature.

def reverse_str(s: str)-> str:
    return s[::-1]

user_input = input("Enter a string to reverse: ")

reverse_output = reverse_str(user_input)
print(f"Reversed String {reverse_output}")


# 🔹 Problem 2: Count Vowels in a String
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
# Example:
# 🔹 Input: "Apple"
# 🔹 Output: 2
# 💡 Hint: Use a loop and check if each character is in a set of vowels.

def vowels_count(s: str)-> str:
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string to count vowels: ")

result = vowels_count(user_input)
print(f"Number of vowels: {result}")


# 🔹 Problem 3: Sum of Digits
# Write a function that takes a non-negative integer and returns the sum of its digits.
# Example:
# 🔹 Input: 1234
# 🔹 Output: 10
# 💡 Hint: Convert the number to a string and iterate over each digit or use modulus and division.


def sum_of_digits(num: int) -> int:
    total = 0
    for digit in str(num):
        total += int(digit)
    return total

user_input = int(input("Enter a number: "))

result = sum_of_digits(user_input)
print(f"Sum of digits: {result}")
