dec = int(input("Enter decimal number: "))

if dec == 0:
    binary = '0'
else:
    remainders = []
    n = dec
    while n > 0:
        remainders.append(str(n % 2))
        n = n // 2
    binary = ''.join(reversed(remainders))

print(f"{dec}(10) = {binary}(2)")
