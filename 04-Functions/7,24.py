def f(expression):
    result = 0
    num = ''
    op = '+'
    for c in expression + '+':
        if c.isdigit():
            num += c
        elif c == '+' or c == '-':
            if num:
                if op == '+':
                    result += int(num)
                elif op == '-':
                    result -= int(num)
            op = c
            num = ''
    return result


print(f("2+3"))
print(f("3+8+1"))
print(f("2+3-4+5-0"))
