
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for number in range(2, 40):
    if is_prime(number):
        print(number, "is a prime!")