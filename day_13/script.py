import numpy as np


def get_data(filename):
    points = []
    folds = []
    with open(filename, "r") as data:
        fold = False
        for line in data:
            if line == "\n":
                fold = True

            if fold == False:
                x, y = line.rstrip("\n").split(",")
                points.append((int(x), int(y)))
            elif fold == True and line != "\n":
                axis, pos = line.rstrip("\n").split("=")
                axis = axis.split(" ")[2]
                folds.append((axis, int(pos)))
    return points, folds


def gen_array(points):
    x = 0
    y = 0
    for p_x, p_y in points:
        if p_x > x:
            x = p_x
        if p_y > y:
            y = p_y
    ret_val = np.zeros((y + 1, x + 1), dtype="bool")
    for p_x, p_y in points:
        ret_val[(p_y, p_x)] = True
    return ret_val


def fold(sheet, axis, pos):
    if axis == "y":
        top = sheet[0:pos, :]
        bottom = np.flip(sheet[pos + 1 :, :], axis=0)
        return top + bottom
    if axis == "x":
        left = np.flip(sheet[:, 0:pos], axis=1)
        right = sheet[:, pos + 1 :]
        return left + right


points, folds = get_data("day_13/data.txt")

sheet = gen_array(points)
axis, pos = folds[0]
new_sheet = fold(sheet, axis, pos)

print(f"Number of points after first fold: np.sum(new_sheet)")

for axis, pos in folds:
    sheet = fold(sheet, axis, pos)

sheet = np.flip(sheet, axis=1)

y_size, x_size = sheet.shape

for y in range(0, (y_size)):
    line = ""
    for x in sheet[y]:
        if x:
            line += "#"
        else:
            line += " "
    print(line)
