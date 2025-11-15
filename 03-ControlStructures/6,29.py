N = int(input("Enter the value of N: "))

primes_found = 0
number = 2

while primes_found < N:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=' ')
        primes_found += 1
    number += 1
