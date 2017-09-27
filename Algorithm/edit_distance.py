def create_matrix(n, m):
    matrix = [[0 for x in range(m + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        matrix[i][0] = i
    for i in range(1, m + 1):
        matrix[0][i] = i
    return matrix


def print_alignment(s1, s2, matrix, n, m):
    temp_s1 = []
    temp_s2 = []
    i, j = n, m
    while i > 0 or j > 0:
        if s1[i - 1] == s2[j- 1]:
            temp_s1.append(s1[i - 1])
            temp_s2.append(s2[j - 1])
            i -= 1
            j -= 1
        else:
            minimum = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
            if minimum == matrix[i - 1][j]:
                temp_s1.append(s1[i - 1])
                temp_s2.append('-')
                i -= 1
            elif minimum == matrix[i][j - 1]:
                temp_s1.append('-')
                temp_s2.append(s2[j - 1])
                j -= 1
            else:
                temp_s1.append(s1[i - 1])
                temp_s2.append(s2[j - 1])
                i -= 1
                j -= 1

    print(temp_s1)
    print(temp_s2)
    return temp_s1, temp_s2


def find_edit_distance(s1, s2, n, m):
    dist_matrix =create_matrix(n, m)
    s1.reverse()
    s2.reverse()
    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dist_matrix[i + 1][j + 1] = dist_matrix[i][j]
            else:
                minimum = min(dist_matrix[i][j],
                              dist_matrix[i + 1][j], dist_matrix[i][j + 1],)
                dist_matrix[i + 1][j + 1] = 1 + minimum
    return dist_matrix


def main():
    s1 = ['s', 'u', 'n', 'n', 'y']
    s2 = ['s', 'n', 'o', 'w', 'y']
    # S1 = 'c a t'
    # S2 = 'c u t'
    count = 0
    # s1 = list(S1.split(' '))
    # s2 = list(S2.split(' '))
    dist_matrix = find_edit_distance(s1, s2, len(s1), len(s2))
    temp1, temp2 = print_alignment(s1, s2, dist_matrix, len(s1), len(s2))
    for x in range(len(temp1)):
        if not temp1[x] == temp2[x]:
            count +=1
    print(count)


if __name__ == '__main__':
    main()
