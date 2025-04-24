def check_parentheses(expression):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in expression:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


print(check_parentheses("(2 + 3) * [5 - (4 / 2)]"))  # True
print(check_parentheses("(2 + 3]"))  # False