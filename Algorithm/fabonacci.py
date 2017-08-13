from functools import lru_cache


class Fibonacci:

    fibonacci_cache = {}

    def fibonacci_value(self, n):
        """This is function to print Fibonacci value of a number at Given position
            This function is coded in python 3.5. """
        # check for integer
        if not isinstance(n, int):
            raise TypeError("Please only enter integer")
        if n <= 0:
            raise ValueError("Kindly Enter positive integer only ")

        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.fibonacci_value(n - 1) + self.fibonacci_value(n - 2)

    def fibonacci_iter(self, n):
        """This function print the fabo series till the given integer"""
        # check for integer
        if not isinstance(n, int):
            raise TypeError("Please only enter integer")
        if n <= 0:
            raise ValueError("Kindly Enter positive integer only ")

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
            for num in range(n - 2):
                term = last_digit + now
                print(term)
                last_digit = now
                now = term

    def fabonacci_explicit_momization(self, n):
        # check for integer
        if not isinstance(n, int):
            raise TypeError("Please only enter integer")
        if n <= 0:
            raise ValueError("Kindly Enter positive integer only ")

        # # Reusing value value from Cache
        if n in self.fibonacci_cache:
            print(self.fibonacci_cache[n])
            return self.fibonacci_cache[n]

        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            value = self.fibonacci_value(n - 1) + self.fibonacci_value(n - 2)
            self.fibonacci_cache[n] = value
            return value

    @lru_cache(maxsize=None)
    def fabonacci_using_functoolcache(self, n):
        # check for integer
        if not isinstance(n, int):
            raise TypeError("Please only enter integer")
        if n < 0:
            raise ValueError("Kindly Enter positive integer only ")
        if n < 2:
            return n
        return self.fabonacci_using_functoolcache(n - 1) + self.fabonacci_using_functoolcache(n - 2)


if __name__ == "__main__":

    # Creating object of our fabonacci class
    fibonacci = Fibonacci()
    print("""Enter your Choice
            1 - Printing nth term of fibonacci
            2 - Printing whole Series till nth term iterative Way (Fast).
            3 - Printing Whole series till nth term in recursive way
            4 - Printing Whole series till nth term in recursive way(Fast Memorization)""")
    choice = int(input())
    print("Enter the number")
    number = int(input())
    if choice == 1:
        print(fibonacci.fibonacci_value(number))
    if choice == 2:
        fibonacci.fibonacci_iter(number)
    if choice == 3:
        for x in range(1, number+1):
            print(fibonacci.fabonacci_explicit_momization(x))
    if choice == 4:
        for x in range(1, number + 1):
            print(fibonacci.fabonacci_using_functoolcache(x))




