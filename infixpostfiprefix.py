def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []  
    result = []  
    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  
        else:
            while stack and precedence(char) <= precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)
    
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

def infix_to_prefix(expression):
    expression = expression[::-1]
    
    expression = expression.replace('(', ')')
    expression = expression.replace(')', '(')
    
    postfix = infix_to_postfix(expression)
    
    prefix = postfix[::-1]
    return prefix

if __name__ == "__main__":
    infix_expression = input("Enter an infix expression: ")

    postfix = infix_to_postfix(infix_expression)
    prefix = infix_to_prefix(infix_expression)

    print(f"Infix Expression: {infix_expression}")
    print(f"Postfix Expression: {postfix}")
    print(f"Prefix Expression: {prefix}")
