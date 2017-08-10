def fibonacci(n):
    """This is function to print Fibonacci value of a number at Given position
        This function is coded in python 3.5. """
    
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def print_fabonacci_series(n):
    """This function print the fabo series till the given integer"""
    if n == 0:
        print("Nothing to show")
    if n == 1:
        print("1 ")
    if n == 2:
        print("1\n1")
    else:
        print("1\n1")
        last_digit = 1
        now = 1
        for num in range(n-2):
            term = last_digit + now
            print(term)
            last_digit = now
            now = term


if __name__ == "__main__":
    print("""Enter your Choice 
            1 - Printing nth term of fabonnici
            2 - Printing whole Series till nth term.""")
    choice = int(input())
    print("Enter the number")
    number = int(input())
    print(fibonacci(number)) if choice == 1 else print_fabonacci_series(number)


