from bubble_sort import bubble_sort
import random
import timeit
from timeit import Timer

# choose a number between 5 and 5000000
list_of_array = []
temp_list = []
bubble_running_time = []
random_number = random.randint(5, 10)

for x in range(0, 11):
    temp_list = []
    for y in range(0, random_number):
        temp_list.append(random.randint(5, 500))
    list_of_array.append(temp_list)

for x in range(0, 11):

# # print(float(sum(bubble_running_time))/len(bubble_running_time))
# # print(bubble_running_time)
