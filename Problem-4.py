#  Problem 4:  Swap two Strings Without Using any Third Variable
#  Input: a = "Hello", b = "World".
# Output: Strings after swap: a = World and b = Hello

#  Problem 5: Swap two numbers without using a temporary variable
#  Input:integer a = "10", b = "50".
# Output: Strings after swap: a = 50 and b = 10


a = "Hello"
b = "World"

print(f"Strings before swap-> a = {a} and b = {b}")

a = a + b  # Concatenate a and b
b = a[:len(a) - len(b)] 
a = a[len(b):] 

print(f"Strings after swap-> a = {a} and b = {b}")
