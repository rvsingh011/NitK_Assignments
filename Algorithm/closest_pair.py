from math import sqrt
import time


def brute_force(points, n):
    least = 100000
    pos1, pos2 = 0, 0
    for x in range(0, n):
        x1, y1 = int(points[x][0]), int(points[x][1])
        for y in range(0, n):
            if x == y:
                pass
            else:
                x2, y2 = int(points[y][0]), int(points[y][1])
                distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                if distance < least:
                    least = distance
                    pos1 = x
                    pos2 = y
    return pos1, pos2, least

if __name__ == "__main__":
    dic = {}
    print("enter the number of points")
    number = int(input())
    for x in range(0, number):
        dic[x] = input().strip().split(",")
    t0 = time.time()
    q, w, r = brute_force(dic, number)
    t1 = time.time()
    print(dic[q], dic[w], r, (t1-t0)/3600)
