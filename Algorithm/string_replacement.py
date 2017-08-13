def replacement(one, two, three):
    return one.replace(two, three)

if __name__ == "__main__":
    print("Enter the string One")
    one = input()
    print("Enter the string two")
    two = input()
    print("Enter the string three")
    three = input()
    print(replacement(one, two, three))
