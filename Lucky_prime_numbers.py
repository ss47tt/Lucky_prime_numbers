import csv
import math

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for start in range(2, int(math.sqrt(limit)) + 1):
        if primes[start]:
            for multiple in range(start * start, limit + 1, start):
                primes[multiple] = False
    return primes

def is_lucky(n):
    digits = str(n)
    if len(digits) % 2 != 0:
        return False  # Ensures equal split
    half = len(digits) // 2
    return sum(map(int, digits[:half])) == sum(map(int, digits[half:]))

def generate_lucky_prime_numbers(start, end):
    primes = sieve_of_eratosthenes(end)
    return [
        num for num in range(start, end + 1)
        if num < 84800000 or num > 84899999  # Exclude the range
        if primes[num] and is_lucky(num)
    ]

def save_lucky_primes_csv(start, end, filename):
    lucky_primes = generate_lucky_prime_numbers(start, end)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Lucky Prime Numbers"] * 10)
        row = []
        for num in lucky_primes:
            row.append(num)
            if len(row) == 10:
                writer.writerow(row)
                row = []
        if row:
            writer.writerow(row)

start = 84790000
end = 84929999
save_lucky_primes_csv(start, end, "lucky_primes.csv")