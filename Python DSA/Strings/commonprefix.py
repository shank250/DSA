from typing import List

def commonPrefix(input: List[str], n: int) -> str:
    strings = input
    if not strings:
        return ""

    reference_str = strings[0]

    common_prefix = ""
    for i in range(len(reference_str)):
        char = reference_str[i]
        if all(i < len(s) and s[i] == char for s in strings[1:]):
            common_prefix += char
        else:
            break
    if common_prefix == "":
        return -1
    return common_prefix

# # Example usage
# strings = ["Codingninjas", "Coding", "Coders", "Codezen"]
# result = longest_common_prefix(strings)
# print("Sample Output 1:")
# print(result)
# like for the above example the output will be
# Cod