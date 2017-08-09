def fact_recursive(n):
    """This function calculate factorial recursively. This one is coded in
        Python 3.5"""
    if n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)

if __name__ == "__main__":
    print("Enter the number")
    number = int(input())
    factorial = fact_recursive(number)
    print(factorial)