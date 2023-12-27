# Find the number that appears once
def find_single_element(arr):
    # Using XOR to find the single element
    result = 0
    for num in arr:
        result ^= num
    return result

# Sample Input 1
input_arr = [1, 1, 2, 2, 3]

# Sample Output 1
output = find_single_element(input_arr)

print("Sample Output 1:")
print(output)
