def bubble_sort(list_of_numbers, range_of_list):
    for i in range(0, range_of_list):
        for j in range(0, range_of_list-1):
            if list_of_numbers[j] > list_of_numbers[j+1]:
                swap(list_of_numbers, j, j+1)
    return list_of_numbers


def swap(list_of_numbers, j, j_next):
    dummy_var = list_of_numbers[j_next]
    list_of_numbers[j_next] = list_of_numbers[j]
    list_of_numbers[j] = dummy_var


if __name__ == "__main__":
    array = []
    sorted_list = []
    print("Enter the range of array")
    number_of_elements = int(input())
    for temp in range(0, number_of_elements):
        array.append(int(input()))
    sorted_list = bubble_sort(array, number_of_elements)
    for num in sorted_list:
        print(num)


# One line logic if don't want a function call but disturb readablity
# list_of_numbers[j], list_of_numbers[j + 1] = list_of_numbers[j + 1], list_of_numbers[j]