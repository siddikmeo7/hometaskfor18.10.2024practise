def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_primes(numbers):
    i = 0
    while i < len(numbers):
        if is_prime(numbers[i]):
            numbers.pop(i)
        else:
            i += 1

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
remove_primes(numbers)
print(numbers)
