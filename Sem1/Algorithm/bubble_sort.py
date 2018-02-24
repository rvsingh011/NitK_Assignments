def bubble_sort(list_of_numbers, range_of_list):
    for i in range(0, range_of_list):
        for j in range(0, range_of_list-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                swap(list_of_numbers, j, j+1)
    return list_of_numbers


def selection_sort(list_of_number, range_of_list):
    for i in range(0, range_of_list):
        smallest = list_of_number[i]
        changed = False
        for j in range(i, range_of_list):
            if list_of_number[j] < smallest:
                smallest = list_of_number[j]
                changed = True
                pos = j
        if changed:
            swap(list_of_number, i, pos)

    return list_of_number


def swap(list_of_numbers, j, j_next):
    dummy_var = list_of_numbers[j_next]
    list_of_numbers[j_next] = list_of_numbers[j]
    list_of_numbers[j] = dummy_var


if __name__ == "__main__":
    array = []
    sorted_list = []
    print("Enter the range of array")
    number_of_elements = int(input())
    print("Enter 1 for bubble and 2 for selection")
    choice = int(input())
    print("Enter the array")
    for temp in range(0, number_of_elements):
        array.append(int(input()))
    if choice == 1:
        sorted_list = bubble_sort(array, number_of_elements)
    elif choice == 2:
        sorted_list = selection_sort(array, number_of_elements)
    for num in sorted_list:
        print(num)


# One line logic if don't want a function call but disturb readablity
# list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]