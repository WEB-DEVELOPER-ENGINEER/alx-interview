def check_brackets(s):
    stack = []
    for i, char in enumerate(s):
        if char in '([{':
            stack.append((char, i+1))
        elif char in ')]}':
            if not stack:
                return i+1
            top = stack.pop()[0]
            if (top == '(' and char != ')') or \
               (top == '[' and char != ']') or \
               (top == '{' and char != '}'):
                return i+1
    if stack:
        return stack[0][1]
    return 'Success'

if __name__ == "__main__":
    print(check_brackets(input()))