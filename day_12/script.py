import copy


class cave:
    def __init__(self, name: str) -> None:
        self.name = name
        self.connections = []
        if name[0].islower():
            self.small = True
        else:
            self.small = False

    def add_connection(self, cave: str) -> None:
        self.connections.append(cave)

    def __str__(self) -> str:
        return self.name


caves = []


def read_data(filename):
    with open(filename, "r") as data:
        for line in data:
            cave_one, cave_two = line.rstrip("\n").split("-")
            known_cave = [cave for cave in caves if cave.name == cave_one]
            if len(known_cave) == 0:
                new_cave = cave(cave_one)
                new_cave.add_connection(cave_two)
                caves.append(copy.deepcopy(new_cave))
            else:
                known_cave[0].add_connection(cave_two)
            known_cave = [cave for cave in caves if cave.name == cave_two]
            if len(known_cave) == 0:
                new_cave = cave(cave_two)
                new_cave.add_connection(cave_one)
                caves.append(copy.deepcopy(new_cave))
            else:
                known_cave[0].add_connection(cave_one)


def walk(path, cave_to_walk, small_caves):
    # Stop conditions
    # start - end -> true
    # start 2 times -> false
    # small cave 2 times - > false
    path.append(cave_to_walk.name)
    stop = False
    single_twice = False
    if "start" in path and "end" in path:
        print(path)
        return

    for check_cave in small_caves:
        if single_twice == False:
            if len([con for con in path if con == check_cave]) == 2:
                single_twice = True
            elif len([con for con in path if con == check_cave]) >= 2:
                stop = True
                break
        else:
            x = [con for con in path if con == check_cave]
            if len(x) >= 2:
                stop = True
                break

    if stop:
        return
    else:
        next_caves = []
        for x in cave_to_walk.connections:
            next_caves.append([cave for cave in caves if cave.name == x][0])
        for next_cave in next_caves:
            walk(copy.deepcopy(path), next_cave, small_caves)


read_data("day_12/data.txt")
small_caves = [cave.name for cave in caves if cave.small]
small_caves.remove("start")
small_caves.remove("end")

# remove end connections
[cave for cave in caves if cave.name == "end"][0].connections = []
# Remove backward to start
for cave in caves:
    if cave.name != "start":
        if "start" in cave.connections:
            cave.connections.remove("start")


walk([], [cave for cave in caves if cave.name == "start"][0], small_caves)
