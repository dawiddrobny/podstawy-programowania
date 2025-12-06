import queue

def reverse_string(text):
    stack = queue.LifoQueue()
    for char in text:
        stack.put(char)
    
    reversed_text = ""
    while not stack.empty():
        reversed_text += stack.get()
    
    return reversed_text

text = input("Enter text to reverse: ")
print(f"Reversed: {reverse_string(text)}")
