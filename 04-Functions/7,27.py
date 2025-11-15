def f(product_code):
    if len(product_code) != 4:
        return False
    digits = [int(d) for d in product_code]
    checksum = (digits[0] + digits[1] + digits[2]) % 7
    return checksum == digits[3]


print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))
