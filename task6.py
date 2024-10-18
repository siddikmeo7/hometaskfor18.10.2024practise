def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def divisors_dict(numbers):
    result = {}
    for num in numbers:
        result[num] = count_divisors(num)
    return result

numbers = [10, 15, 21, 30]
divisors = divisors_dict(numbers)
print(divisors)
