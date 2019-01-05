def isBalanced(input_string):
    signs = {
        "{":"}",
        "}":"{",
        "[":"]",
        "]":"[",
        "(":")",
        ")":"("
    }
    
    stack = []
    
    for i in range(len(input_string)):
        if stack and input_string[i] == signs[stack[-1]]:
            stack.pop()
        else:
            stack.append(input_string[i])

    if not stack:
        return True
    return False

sequence = input("Enter the sequence: ")
print(isBalanced(sequence))