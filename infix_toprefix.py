def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def is_operator(c):
    return c in "+-*/"

def infix_to_prefix(expression):
    # Step 1: Reverse the infix expression
    expression = expression[::-1]

    # Step 2: Replace '(' with ')' and vice versa
    expression = expression.replace('(', '#')
    expression = expression.replace(')', '(')
    expression = expression.replace('#', ')')

    stack = []
    result = []

    # Step 3: Convert to postfix (on reversed expression)
    for ch in expression:
        if ch.isalnum():  # operand (number/letter)
            result.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            if stack:  # discard the '('
                stack.pop()
        elif is_operator(ch):
            while stack and precedence(ch) < precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(ch)

    # Pop remaining operators
    while stack:
        result.append(stack.pop())

    # Step 4: Reverse the result to get prefix
    return ''.join(result[::-1])

# Example usage
infix_expr = "(a+b)*c"
print("Infix expression:", infix_expr)
print("Prefix expression:", infix_to_prefix(infix_expr))
