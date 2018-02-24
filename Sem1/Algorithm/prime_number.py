from math import sqrt, floor, ceil


def prime_number(n):
    """This function calculate whether the number is prime or not"""
    if not isinstance(n, int):
        raise TypeError("Enter the correct type")
    if n < 1:
        raise ValueError("Enter a positive Integer Greater than 0")
    if n == 1:
        return "One is nor Prime nor Composite"
    else:
        for x in range(2,n):
            if n % x == 0:
                return "Non Prime"
        return "Prime"


def prime_sqrt(n):
    """This function is O(root n)"""
    if type(n) != int:
        raise TypeError("Enter the correct type")
    if n < 1:
        raise ValueError("Enter a positive Integer")
    if n == 1:
        return "One is nor Prime nor Composite"
    max_divisor = floor(sqrt(n))
    for x in range(2, 1+max_divisor):
        if n % x == 0:
            return "Non prime"
    else:
        return "prime"


def prime_effective(n):
    """This is the most effective prime function"""
    if type(n) != int:
        raise TypeError("Enter the correct type")
    if n < 1:
        raise ValueError("Enter a positive Integer")
    if n == 1:
        return "One is not prime nor composite"
    if n % 2 == 0:
        if n == 2:
            return "Prime"
        else:
            return "Non prime"
    else:
        max_divisor = floor(sqrt(n))
        for x in range(2, 1 + max_divisor,2):
            if n % x == 0:
                return "Non prime"
        return "Prime"

if __name__ == "__main__":
    count = 0
    print("""Enter the number you want to check""")
    number = int(input())
    print("""Enter the method 1(normal), 2)sqrt, 3)most effective""")
    choice = int(input())
    if choice == 1:
        print(prime_number(number))
    elif choice == 2:
        print(prime_sqrt(number))
    elif choice == 3:
        print(prime_effective(number))


