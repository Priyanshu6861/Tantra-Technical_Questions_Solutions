
#  Problem 3:  Biggest and smallest number in an array
#  Write a program to print the biggest and smallest number in the array. 

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: Maximum is: 5
# Minimum is: 1

# Input: arr[] = {5, 3, 7, 4, 2}
# Output: Maximum is: 7
# Minimum is: 2


def find_min_max(arr):
    if not arr:
        return None, None 
    
    max_num = min_num = arr[0] 
    
    for num in arr:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num    
    return max_num, min_num

# Example 1
arr1 = [1, 2, 3, 4, 5]
ans = find_min_max(arr1)
print(f"Maximum is: {ans[0]}")
print(f"Minimum is: {ans[1]}")

# Example 2
arr2 = [5, 3, 7, 4, 2]
ans = find_min_max(arr2)
print(f"Maximum is: {ans[0]}")
print(f"Minimum is: {ans[1]}")
