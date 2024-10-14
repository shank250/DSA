s = str("[()]{}{[()()]()})")

stack = []
for i in s:
    if i == "[" or i == "(" or i == "{" :
        stack.append(i)
    elif i == "]" or i == ")" or i == "}":
        if len(stack) == 0:
            result = "Not Balanced"
            break
        j = stack.pop()
        if i == "]" and j != "[" :
            result = "Not Balanced"
            break
        elif i == "}" and j != "{" :
            result = "Not Balanced"
            break
        elif i == ")" and j != "(" :
            result = "Not Balanced"
            break
        else:
            result = "Balanced"
if len(stack) != 0 :
    result = "Not Balanced"
print(result)