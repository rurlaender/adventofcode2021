input = []
with open("day_06/data.txt", "r") as data:
    for val in data.readline().split(","):
        input.append(int(val))

fishes = []
fish_age = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for nbr in input:
    fish_age[nbr] += 1


def calc_lantern_population(fishes, days):
    fish_age = fishes[:]
    for day in range(0, days):
        copy = fish_age[:]
        for i, nbr_fish in enumerate(copy):
            if i == 6:
                fish_age[i] = copy[i + 1] + copy[0]
            elif i == 8:
                fish_age[i] = copy[0]
            else:
                fish_age[i] = copy[i + 1]
    print(sum(fish_age))


calc_lantern_population(fish_age, 80)
calc_lantern_population(fish_age, 256)
