import queue


def decimal_to_binary(n):
    stack = queue.LifoQueue()

    # Handle 0 case
    if n == 0:
        stack.put(0)

    temp_n = n
    while temp_n > 0:
        remainder = temp_n % 2
        stack.put(remainder)
        temp_n = temp_n // 2

    binary_string = ""
    while not stack.empty():
        binary_string += str(stack.get())

    return binary_string


# Allow user input
try:
    user_input = int(input("\nEnter a natural number to convert: "))
    print(f"Binary number: {decimal_to_binary(user_input)}")
except ValueError:
    print("Please enter a valid integer.")
