# Men Favourable minimal matching
from random import choice
import copy

pref_matrix_boys = {}
pref_matrix_girls = {}
men_patner = {}
girl_patner = {}


def propose(boy_name, men_patner, girl_patner, pref_matrix_girls, pref_matrix_boys):
    girl_name = pref_matrix_boys[boy_name][0]
    if not girl_patner[pref_matrix_boys[boy_name][0]]:
        print(girl_name)
        pref_matrix_boys[boy_name].remove(girl_name)
        men_patner[boy_name] = girl_name
        girl_patner[girl_name] = boy_name
    else:
        index_of_current_bf = pref_matrix_girls[girl_name].index(girl_patner[girl_name])
        new_bf_index = pref_matrix_girls[girl_name].index(boy_name)
        if new_bf_index < index_of_current_bf:
            ex_bf = girl_patner[girl_name]
            girl_patner[girl_name] = boy_name
            men_patner[ex_bf] = None
            men_patner[boy_name] = girl_name
            pref_matrix_boys[boy_name].remove(girl_name)
            propose(ex_bf, men_patner, girl_patner, pref_matrix_girls, pref_matrix_boys)
        else:
            pref_matrix_boys[boy_name].remove(girl_name)
            propose(boy_name, men_patner, girl_patner, pref_matrix_girls, pref_matrix_boys)


if __name__ == "__main__":
    list_boys = ['Zeus', 'Victor', 'Wyatt', 'Yancey', 'Xavier']
    list_girls = ['Diane', 'Bertha', 'Amy', 'Clare', 'Erika']
    temp_boys = []
    temp_girls = []
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
        pref_matrix_boys[list_boys[x]] = pref_matrix_boys_temp[x]
    for x in range(len(pref_matrix_girls_temp)):
        pref_matrix_girls[list_girls[x]] = pref_matrix_girls_temp[x]

    # pref_matrix_girls = {'Amy': ['Zeus', 'Victor', 'Wyatt', 'Yancey', 'Xavier'],
    #          'Bertha': ['Xavier', 'Wyatt', 'Yancey', 'Victor', 'Zeus'],
    #          'Clare': ['Wyatt', 'Xavier', 'Yancey', 'Zeus', 'Victor'],
    #          'Diane': ['Victor', 'Zeus', 'Yancey', 'Xavier', 'Wyatt'],
    #          'Erika': ['Yancey', 'Wyatt', 'Zeus', 'Xavier', 'Victor']
    #          }
    #
    # pref_matrix_boys = {'Victor': ['Bertha', 'Amy', 'Diane', 'Erika', 'Clare'],
    #         'Wyatt': ['Diane', 'Bertha', 'Amy', 'Clare', 'Erika'],
    #         'Xavier': ['Bertha', 'Erika', 'Clare', 'Diane', 'Amy'],
    #         'Yancey': ['Amy', 'Diane', 'Clare', 'Bertha', 'Erika'],
    #         'Zeus': ['Bertha', 'Diane', 'Amy', 'Erika', 'Clare']
    #         }
    men_patner = dict((list_boys[i], None) for i in range(len(list_boys)))
    girl_patner = dict((list_girls[i], None) for i in range(len(list_girls)))
    for i in list_boys:
        propose(i, men_patner, girl_patner, pref_matrix_girls, pref_matrix_boys)
    print(girl_patner)























