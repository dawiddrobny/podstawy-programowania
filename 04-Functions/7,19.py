def f(number):
    digits = str(number)
    count = {}
    for d in digits:
        count[d] = count.get(d, 0) + 1
    total = 0
    for d, freq in count.items():
        if freq > 1:
            total += int(d) * freq
    return total


print(f(1027))
print(f(230335))
print(f(513553007))
