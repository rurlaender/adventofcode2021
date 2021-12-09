import numpy as np


def get_data(filename):
    data = []
    y = 0
    with open(filename, "r") as data_file:
        for line in data_file:
            line = line.rstrip("\n")
            x_size = len(line)
            data.append([])
            for i in range(0, x_size):
                data[y].append(int(line[i]))
            y += 1
    return data


data = get_data("day_09/data.txt")
y_size = len(data)
x_size = len(data[1])
result = 0

# Another, easier way could be to add a surrounding frame of 9.
# Than it's not necessary to look on all the edge cases

for y in range(0, y_size):
    for x in range(0, x_size):
        point = data[y][x]
        if y == 0 and x == 0:
            if point < data[0][1] and point < data[1][0]:
                result += point + 1
        elif y == 0 and 0 < x < x_size - 1:
            if (
                point < data[y][x - 1]
                and point < data[y][x + 1]
                and point < data[y + 1][x]
            ):
                result += point + 1
        elif y == 0 and x == x_size - 1:
            if point < data[0][x - 1] and point < data[1][x]:
                result += point + 1
        elif 0 < y < y_size - 1 and x == 0:
            if (
                point < data[y - 1][x]
                and point < data[y + 1][x]
                and point < data[y][x + 1]
            ):
                result += point + 1
        elif 0 < y < y_size - 1 and x == x_size - 1:
            if (
                point < data[y - 1][x]
                and point < data[y + 1][x]
                and point < data[y][x - 1]
            ):
                result += point + 1
        elif y == y_size - 1 and x == 0:
            if point < data[y - 1][x] and point < data[y][x + 1]:
                result += point + 1
        elif y == y_size - 1 and 0 < x < x_size - 1:
            if (
                point < data[y][x - 1]
                and point < data[y][x + 1]
                and point < data[y - 1][x]
            ):
                result += point + 1
        elif y == y_size - 1 and x == x_size - 1:
            if point < data[y - 1][x] and point < data[y][x - 1]:
                result += point + 1
        else:
            if (
                point < data[y - 1][x]
                and point < data[y + 1][x]
                and point < data[y][x - 1]
                and point < data[y][x + 1]
            ):
                result += point + 1


print(result)

from scipy.ndimage import measurements

area = np.array(data)
area = area + 1
area = np.where(area == 10, 0, area)
map, areas = measurements.label(area)
area_size = []
for area in range(1, areas + 1):
    area_size.append(np.count_nonzero(map == area))

area_size.sort(reverse=True)
print(area_size[0] * area_size[1] * area_size[2])
