#Q1
def multiples_of_3_and_5_sum(limit):
    total = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


limit = 10
result = multiples_of_3_and_5_sum(limit)
print(f"Solution for parameter value {limit}: {result}")

#Q2
def even_fibonacci_sum(limit):
    fib_sum = 0
    a, b = 1, 2  

    while b <= limit:
        if b % 2 == 0:
            fib_sum += b
        a, b = b, a + b 

    return fib_sum

limit = 4000000
result = even_fibonacci_sum(limit)
print(f"The sum of even-valued Fibonacci terms not exceeding {limit}: {result}")


#Q3
def largest_prime_factor(number):
    prime_factor = 2
    while prime_factor * prime_factor <= number:
        if number % prime_factor == 0:
            number //= prime_factor
        else:
            prime_factor += 1
    return number

number = 13195
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")

#Q4
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product(n):
    max_num = 10 ** n - 1
    min_num = 10 ** (n - 1)
    largest_palindrome = 0

    for i in range(max_num, min_num - 1, -1):
        for j in range(i, min_num - 1, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome

# For example, let's find the largest palindrome made from the product of two 3-digit numbers:
n = 3
result = largest_palindrome_product(n)
print(f"The largest palindrome made from the product of two {n}-digit numbers is: {result}")

#Q5

import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(n):
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

# For example, let's find the smallest positive number divisible by all numbers from 1 to 10:
n = 10
result = smallest_multiple(n)
print(f"The smallest positive number divisible by all numbers from 1 to {n} is: {result}")
