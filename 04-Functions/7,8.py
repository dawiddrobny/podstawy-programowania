def f(amount_to_pay):
    coins = 0
    for coin in [5, 2, 1]:
        count, amount_to_pay = divmod(amount_to_pay, coin)
        coins += count
    return coins


print(f(23))
print(f(8))
print(f(2))
print(f(0))
