def fact_iter(n):
    """This function will find the Factorial of the given number by iterative
        method. This function is coded in Pyhton 3.5."""
    temp = 1
    for num in range(1,n):
        temp += temp * num
    return temp

if __name__ == "__main__":
    print("Enter the number")
    number = int(input())
    number = fact_iter(number)
    print(number)