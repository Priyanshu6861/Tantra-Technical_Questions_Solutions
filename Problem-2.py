#  Problem 2:  Determine whether a given string is Palindrome
#  A string “madam” is a palindromic string because it reads the same forwards and backward. 
# Input: “anna”
# Output: true

# Input: “India”
# Output: false

# Solution:-


def check_palindrome(str):
    new_str = str.replace(" ", "").lower()
    if new_str == new_str[::-1]:
        return "palindrome"
    else:
        return "not palindrome"

# Example 1
str1 = "anna"
ans = check_palindrome(str1)
print(f"'{str1}' is {ans}")

# Example 2
str2 = "India"
ans = check_palindrome(str2)
print(f"'{str2}' is {ans}")

