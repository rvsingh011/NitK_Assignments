import time
import math


def find_distance(x, y):
    return math.sqrt(math.pow((x[0] - y[0]), 2) + math.pow((x[1] - y[1]), 2))


def brute_force(point):
    # point.sort()
    minimum_dis = 1000
    for i in range(len(point) - 1):
        for j in range(i + 1, len(point)):
            if find_distance(point[i], point[j]) < minimum_dis:
                minimum_dis = find_distance(point[i], point[j])

    return minimum_dis


def strip_closest(strip, n, d):
    minimum = d
    j = 1
    for i in range(n):
        if j < n and (strip[j][1] - strip[i][1]) < minimum:
            for j in range(i + 1, n):
                if find_distance(strip[i], strip[j]) < minimum:
                    minimum = find_distance(strip[i], strip[j])
    return minimum


def find_smallest_dist(X, Y, n):
    if n <= 3:
        return brute_force(X)

    mid = n // 2
    mid_point = X[mid]
    y_l = []
    y_r = []
    for i in range(n):
        if Y[i][0] <= mid_point[0]:
            y_l.append(Y[i])
        else:
            y_r.append(Y[i])
    dl = find_smallest_dist(X, y_l, mid)
    dr = find_smallest_dist(X[mid:], y_r, n - mid)
    d = min(dl, dr)
    strip = []
    for i in range(n):
        if abs(Y[i][0] - mid_point[0]) < d:
            strip.append(Y[i])
    # print(strip)
    return min(d, strip_closest(strip, len(strip), d))


def closest_pair(point, n):
    X = point.copy()
    Y = point.copy()
    X = sorted(X, key=lambda x: x[0])
    Y = sorted(Y, key=lambda x: x[1])
    return find_smallest_dist(X, Y, n)


if __name__ == '__main__':
    point = [[2, 3], [12, 30], [40, 50], [5, 1], [12, 10], [3, 4]]
    start_time = time.time()
    print(closest_pair(point, len(point)))
    elapsed = (time.time() - start_time)/3600
    print(elapsed)