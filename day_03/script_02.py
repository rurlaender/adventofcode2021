import math


numbers = []
with open("day_03/data.txt", "r") as data:
    for line in data:
        numbers.append(int(line, 2))

nbrs = numbers[:]
for pos in range(11, -1, -1):
    counter = 0
    for nbr in nbrs:
        if nbr & int(math.pow(2, pos)) == int(math.pow(2, pos)):
            counter += 1

    if counter >= len(nbrs) - counter:
        bit_val = int(math.pow(2, pos))
    else:
        bit_val = 0

    new_nbrs = []
    for nbr in nbrs:
        if nbr & int(math.pow(2, pos)) == bit_val:
            new_nbrs.append(nbr)
    nbrs = new_nbrs[:]
    if len(nbrs) == 1:
        break


oxygen = nbrs[0]

nbrs = numbers[:]

for pos in range(11, -1, -1):
    counter = 0
    for nbr in nbrs:
        if nbr & int(math.pow(2, pos)) == 0:
            counter += 1

    if counter <= len(nbrs) - counter:
        bit_val = 0
    else:
        bit_val = int(math.pow(2, pos))

    new_nbrs = []
    for nbr in nbrs:
        if nbr & int(math.pow(2, pos)) == bit_val:
            new_nbrs.append(nbr)
    nbrs = new_nbrs[:]
    if len(nbrs) == 1:
        break
co2 = nbrs[0]

print(oxygen, co2, oxygen * co2)
