import math as ma
import collections as co

def add(*numbers):
    """adds numbers up"""
    return sum(numbers)

def subtract(*numbers):
    """subtracts numbers"""
    number_list = list(numbers)
    result = number_list.pop(0)
    for number in number_list:
        result = result - number
    return result

def multiplicate(*numbers):
    """multiplicates numbers"""
    result = 1
    for number in numbers:
        result = result * number
    return result

def divide(*numbers, error=None):
    """divides numbers"""
    number_list = list(numbers)
    result = number_list.pop(0)
    for number in number_list:
        if number:
            result = result / number
        else:
            return error
    return result 
    
def exponentiate(*numbers):
    """raises a number to the power of up to three numbers"""
    number_list = list(numbers)
    result = number_list.pop(0)
    for number in number_list:
        result = result ** number
    return result

    
def isNumberPrime(prime):
    """checks if a number is prime"""
    if prime == 1:
        return False
    for i in range(2, int(ma.sqrt(prime))+1):
        if prime % i == 0:
            return False
    return True

def roundDown(number):
    """rounds a number down"""
    return float(int(number))

def roundUp(number):
    """rounds a number up"""
    return float(int(number)) + 1

def getDivisors(number):
    """returns divisors of a number"""
    divisors = []
    for i in range(0, number):
        if not number % (i + 1):
            divisors.append(i+1)
    return divisors

def getPrimeFactors(number):
    """returns prime factors of a number"""
    prime_factors = []
    while number > 1:
        for i in range(2, int(number)+1):
            if number % i == 0:
                prime_factors.append(i)
                number = number / i
                break
    return prime_factors

def meaningOfLife():
    """no further explanation needed"""
    return 42

def linearFunction(x1, y1, x2, y2):
    """returns the linear formula with the coordinates of two points"""
    m = (y1 - y2)/(x1 - x2)
    n = y1 - x1 * m
    return (m, n)

def sqrt(number):
    """returns the root of a number"""
    return number ** 0.5

def modulo(number, m):
    """returns min non-negative d to: number is congruent to d modulo m"""
    return number % m

def findInvert(number, m):
    """returns d to (number times d) is congruent to 1 modulo m"""
    d = 1
    while True:
        if (d * number - 1) % m == 0:
            break
        else:
            d += 1 
    return d

def isNumberMersenne(number):
    """checks if a number can be written in the form 2^n+1"""
    x = number + 1
    while x != 1:
        x = 0.5 * x
        if x != int(x):
            return False
    return True

def arithmeticMean(*numbers):
    return sum(numbers)/len(numbers)

def median(*numbers):
    """returns the median of the numbers"""
    numbers_list = list(numbers)
    numbers_list.sort()
    if len(numbers_list) % 2:
        return numbers_list[int((len(numbers_list) - 1)/2)]
    else:
        n = len(numbers_list)/2 - 1
        m = len(numbers_list)/2
        return (numbers_list[int(m)] + numbers_list[int(n)])/2
    
def areaTriangle(b, h):
    """returns the area of a triangle by its side lenghts b and its height h"""
    return b * h / 2

def mode(*numbers):
    counter = co.Counter(numbers)
    mode_tuple = [k for k, v in counter.items() if v == max(counter.values())]
    return mode_tuple    