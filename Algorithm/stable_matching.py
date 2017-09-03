from random import choice
import copy
if __name__ == "__main__":
    list_boys = ['Ravi', 'Pankaj', 'Somjeet', 'Appu', 'Akshay']
    list_girls = ['Riya', 'Priya', 'Sonali', 'Richa', 'Mamta']
    temp_boys = []
    temp_girls = []
    pref_matrix_boys = []
    pref_matrix_girls = []
    pref_matrix_boys_temp = [['0' for x in range(len(list_girls))] for y in range(len(list_boys))]
    pref_matrix_girls_temp = [['0' for x in range(len(list_boys))] for y in range(len(list_girls))]
    for x in range(len(pref_matrix_girls_temp)):
        temp_boys = copy.copy(list_boys)
        temp_girls = copy.copy(list_girls)
        for y in range(len(pref_matrix_girls_temp)):
            m = choice(temp_boys)
            n = choice(temp_girls)
            pref_matrix_girls_temp[x][y] = m
            pref_matrix_boys_temp[x][y] = n
            temp_boys.remove(m)
            temp_girls.remove(n)
    for x in range(len(pref_matrix_boys_temp)):
        pref_matrix_boys.append([list_boys[x], pref_matrix_boys_temp[x]])
    for x in range(len(pref_matrix_girls_temp)):
        pref_matrix_girls.append([list_girls[x], pref_matrix_girls_temp[x]])
    print(pref_matrix_boys)
    print(pref_matrix_girls)



