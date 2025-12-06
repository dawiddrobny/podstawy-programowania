import queue


def calculate_rpn(expression):
    stack = queue.LifoQueue()
    tokens = expression.split()

    for token in tokens:
        if token.lstrip('-').replace('.', '', 1).isdigit():  # Check if number
            stack.put(float(token))
        elif token in ['+', '-', '*', '/']:
            val2 = stack.get()
            val1 = stack.get()
            if token == '+':
                stack.put(val1 + val2)
            elif token == '-':
                stack.put(val1 - val2)
            elif token == '*':
                stack.put(val1 * val2)
            elif token == '/':
                if val2 == 0:
                    print("Error: Division by zero")
                    return
                stack.put(val1 / val2)
        elif token == '=':
            if not stack.empty():
                print(f"Result: {stack.get()}")
            else:
                print("Stack empty")


print("Enter RPN expression (space separated, end with =):")
# Example: 2 3 + =
expr = input()
calculate_rpn(expr)
