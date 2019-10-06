# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

limit = 600851475143


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


for x in range(3, limit):
    if limit % x == 0 and is_prime(x):
        print(x)
