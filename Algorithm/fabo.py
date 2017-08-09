def Fibonacci(n):
    """This is function to print Fibonacci value of a number at Given position
        This function is coded in python 2.7. """
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


if __name__ == "__main__":
    print "Enter the Position which you want to find"
    input = int(raw_input())
    print Fibonacci(input)

