# 17. Using range(1,101), make three list,
# one containing all even numbers
# one containing all odd numbers
# One containing only prime numbers.

from math import sqrt

lst_even = []
lst_odd = []
lst_prime = []


def isPrime(n):
    if n < 2:
        return False
    e = int(sqrt(n))
    for i in range(2, e + 1):
        if n % i == 0:
            return False
    return True


for i in range(1, 101):
    if isPrime(i):
        lst_prime.append(i)
    if i % 2 == 0:
        lst_even.append(i)
    else:
        lst_odd.append(i)

for i in lst_prime:
    print(i, end=" ")
print()
for i in lst_even:
    print(i, end=" ")
print()
for i in lst_odd:
    print(i, end=" ")
