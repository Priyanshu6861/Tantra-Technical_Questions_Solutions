# Technical Questions:

# Problem 1: Program to count occurrences of a given character in a string.

#  Count character 'e' in the below string.
# 	Input "geeksforgeeks". 
# 	Output: 4

# 	Count character '3' in the below string.
# 	Input "abccdefgaa."
# 	Output : 3

# Solution:-

def count_character(str, chr):
    count = 0
    for i in str:
        if i == chr:
            count += 1
    return count

str1 = "geeksforgeeks"
c1 = 'e'
ans = count_character(str1, c1)
print(f"Count of {c1} in {str1}: {ans}")

str2 = "abccdefgaa."
c2 = '3'
ans = count_character(str2, c2)
print(f"Count of {c2} in '{str2}': {ans}")


