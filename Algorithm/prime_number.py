from math import sqrt


def prime_number(n):
    """This function calculate whether the number is prime or not"""
    if not isinstance(n, int):
        raise TypeError("Enter the correct type")
    if n <= 1:
        raise ValueError("Enter a positive Integer Greater than 1")
    status_flag = None
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            status_flag = True

    if status_flag:
        return "Not Prime Number"
    else:
        return "Prime Number"


if __name__ == "__main__":
    count = 0
    print("Enter the number you want to check")
    number = int(input())
    print(prime_number(number))
