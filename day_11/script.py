import numpy as np


def get_data(filename):
    file_data = []
    with open(filename, "r") as data:
        for line_nbr, line in enumerate(data):
            file_data.append([])
            for i in range(0, len(line.rstrip("\n"))):
                file_data[line_nbr].append(line[i])
    return np.array(file_data, dtype="int16")


def increment_near(octopuses):
    octopuses = octopuses + 0
    # Get positions
    positions = []
    for y in range(0, 10):
        for x in range(0, 10):
            if octopuses[y][x] == 1:
                positions.append((y, x))
    for position in positions:
        # top left
        if position[0] == 0 and position[1] == 0:
            octopuses[0][1] += 1
            octopuses[1][0] += 1
            octopuses[1][1] += 1
        # top
        elif position[0] == 0 and 0 < position[1] < 9:
            octopuses[0][position[1] - 1] += 1
            octopuses[0][position[1] + 1] += 1
            octopuses[1][position[1] - 1] += 1
            octopuses[1][position[1] + 1] += 1
            octopuses[1][position[1]] += 1
        # top right
        elif position[0] == 0 and position[1] == 9:
            octopuses[0][8] += 1
            octopuses[1][8] += 1
            octopuses[1][9] += 1
        # left
        elif 0 < position[0] < 9 and position[1] == 0:
            octopuses[position[0] - 1][0] += 1
            octopuses[position[0] + 1][0] += 1
            octopuses[position[0] - 1][1] += 1
            octopuses[position[0]][1] += 1
            octopuses[position[0] + 1][1] += 1
        # right
        elif 0 < position[0] < 9 and position[1] == 9:
            octopuses[position[0] - 1][9] += 1
            octopuses[position[0] + 1][9] += 1
            octopuses[position[0] - 1][8] += 1
            octopuses[position[0]][8] += 1
            octopuses[position[0] + 1][8] += 1
        # bottom left
        elif position[0] == 9 and position[1] == 0:
            octopuses[8][0] += 1
            octopuses[8][1] += 1
            octopuses[9][1] += 1
        # bottom
        elif position[0] == 9 and 0 < position[1] < 9:
            octopuses[9][position[1] - 1] += 1
            octopuses[9][position[1] + 1] += 1
            octopuses[8][position[1] - 1] += 1
            octopuses[8][position[1] + 1] += 1
            octopuses[8][position[1]] += 1
        # bottom right
        elif position[0] == 9 and position[1] == 9:
            octopuses[8][8] += 1
            octopuses[8][9] += 1
            octopuses[9][8] += 1
        # all others
        else:
            octopuses[position[0] - 1][position[1] - 1] += 1
            octopuses[position[0] - 1][position[1]] += 1
            octopuses[position[0] - 1][position[1] + 1] += 1
            octopuses[position[0]][position[1] - 1] += 1
            octopuses[position[0]][position[1] + 1] += 1
            octopuses[position[0] + 1][position[1] - 1] += 1
            octopuses[position[0] + 1][position[1]] += 1
            octopuses[position[0] + 1][position[1] + 1] += 1

    return octopuses


octopuses = get_data("day_11/data.txt")
flash_counter = 0

for round in range(0, 500):
    # Increment by one
    octopuses = octopuses + 1
    # Look who's flashing
    allready_flashed = np.zeros((10, 10), dtype="bool")

    while ((octopuses >= 10) ^ allready_flashed).any():
        # Get potential flashers
        pot_flash = octopuses >= 10
        if (pot_flash ^ allready_flashed).any():
            flash = pot_flash ^ allready_flashed
            allready_flashed += pot_flash
            flashing_octopuses = increment_near(flash)
            octopuses = octopuses + flashing_octopuses

    flash_counter += len(octopuses[octopuses >= 10])
    octopuses[octopuses >= 10] = 0

    if len(octopuses[octopuses == 0]) == 100:
        print(round + 1)
        break

print(flash_counter)
