def fact_iter(n):
    """This function will find the Factorial of the given number by iterative
        method. This function is coded in Pyhton 3.5."""

    # check for integer
    if not isinstance(n, int):
        raise TypeError("Please only enter integer")
    if n <= 0:
        raise ValueError("Kindly Enter positive integer only ")

    temp = 1
    for num in range(1,n):
        temp += temp * num
    return temp


def fact_recu(n):
    # check for integer
    if not isinstance(n, int):
        raise TypeError("Please only enter integer")
    if n <= 0:
        raise ValueError("Kindly Enter positive integer only ")
    if n == 1:
        return 1
    else:
        return n * fact_recu(n-1)


if __name__ == "__main__":
    print("""Enter your choice
             1 - factorial Iterative
             2 - factorial Recursive""")
    choice = int(input())
    print("Enter the number")
    number = int(input())
    if choice == 1:
        number = fact_iter(number)
    if choice == 2:
        number = fact_recu(number)
    print(number)