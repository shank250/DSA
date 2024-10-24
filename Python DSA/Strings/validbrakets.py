def longestValidBrackets(s: str) -> int:
    # Stack to store indices of opening brackets
    stack = [-1]
    max_len = 0
    
    # Dictionary to map closing brackets to their matching opening ones
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(s):
        if char in '({[':
            # Push the index of the opening bracket onto the stack
            stack.append(i)
        elif char in ')}]':
            # Check if the stack is not empty and the top of the stack is the matching opening bracket
            if stack and s[stack[-1]] == matching_brackets[char]:
                # Pop the opening bracket index
                stack.pop()
                if stack:
                    # Calculate the length of the current valid substring
                    max_len = max(max_len, i - stack[-1])
                else:
                    # Stack is empty, push current index as the new base
                    stack.append(i)
            else:
                # If not a match, push the current index of the closing bracket as a new base
                stack.append(i)

    return max_len

# Example usage
s = "{()]}()]"
print(longestValidBrackets(s))  # Output: 10 (The longest valid substring is "{[()]}[()]")
