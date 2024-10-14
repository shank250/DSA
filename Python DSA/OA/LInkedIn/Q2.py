# def getMinOperations(change, arr):
#     m = len(arr)
#     n = len(change)
    
#     # Check if arr[] can be turned into NULLs
#     operations = 0
    
#     for i in range(n):
#         idx = change[i] - 1  # convert 1-based index to 0-based
#         if idx >= 0 and arr[idx] == 0:  # if the element can be nullified
#             arr[idx] = None
#         else:
#             # Decrement all non-NULL elements if it's possible
#             for j in range(m):
#                 if arr[j] is not None:
#                     arr[j] = max(0, arr[j] - 1)
        
#         operations += 1
        
#         # Check if all elements have become NULL
#         if all(x is None for x in arr):
#             return operations
    
#     return -1 if any(x is not None for x in arr) else operations
# def getMinOperations(change, arr):
#     n = len(change)
#     m = len(arr)
    
#     # Initialize operations count
#     operations = 0
    
#     # Create a copy of arr to modify
#     current_arr = arr.copy()
    
#     # Continue until all elements are NULL or we've used all operations
#     while any(x is not None and x != 0 for x in current_arr) and operations < n:
#         # Get the current change value
#         curr_change = change[operations]
        
#         # Process elements that can be changed in this operation
#         for i in range(min(curr_change, m)):
#             if current_arr[i] is not None:
#                 if current_arr[i] > 0:
#                     # Decrement the element
#                     current_arr[i] = max(0, current_arr[i] - 1)
#                 elif current_arr[i] == 0:
#                     # Change to NULL if it's 0
#                     current_arr[i] = None
        
#         operations += 1
    
#     # Check if all elements are NULL or 0
#     if all(x is None or x == 0 for x in current_arr):
#         return operations
#     else:
#         return -1

def getMinOperations(change, arr):
    n = len(arr)
    m = len(change)
    
    # Track indices that can be changed to NULL
    can_change = set(change)
    
    operations = 0
    nullified = [False] * n  # To track which elements have been turned to NULL
    
    while True:
        made_change = False
        
        for i in range(n):
            if arr[i] > 0:
                arr[i] -= 1  # Decrement operation
                operations += 1
                made_change = True
            
            if arr[i] == 0 and i in can_change and not nullified[i]:
                nullified[i] = True  # Turn to NULL
                operations += 1
                made_change = True
        
        # Check if all elements are NULL now
        if all(nullified):
            return operations
        
        # If no changes are made and we still have non-NULL elements
        if not made_change:
            return -1

# Example usage:
# change = [0, 1, 0, 2]
# arr = [1, 1]
# result = getMinOperations(change, arr)
# print(result)  # Output: 4

# # Example usage:
# change = [0, 1, 0, 2]
# arr = [1, 1]
# result = getMinOperations(change, arr)
# print(result)  # Output: 4
# # Example usage:
# change = [0, 1, 0, 2]
# arr = [1, 1]
# result = getMinOperations(change, arr)
# print(result)  # Output: 4

change = [0, 0, 0, 2, 1, 3, 2]
arr = [1, 3, 2]

# result = min_operations_to_nullify(change, arr)
# print(f"Minimum number of operations required: {result}")


# Example usage
# change = [1, 0, 1, 3, 2, 1, 0, 3, 1, 1]
# arr = [2, 1, 2]

result = getMinOperations(change, arr)
print(result)  # Output should be 4
