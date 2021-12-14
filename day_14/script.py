import copy


def get_data(filename):
    template = ""
    insertions = {}
    with open(filename, "r") as data:
        fold = False
        for line in data:
            if line == "\n":
                fold = True
            if fold == False:
                template = line.rstrip("\n")
            elif fold == True and line != "\n":
                x, y = line.rstrip("\n").split(" -> ")
                insertions[x] = y
    return template, insertions


template, insertions = get_data("day_14/data.txt")

polymer = {}

for a, b in zip(template, template[1:]):
    polymer[a + b] = polymer.get(a + b, 0) + 1

poly_temp = {}

for i in range(0, 40):
    poly_temp = {}
    for couple, count in polymer.items():
        insertion = insertions[couple]
        poly_temp[couple[0] + insertion] = (
            poly_temp.get(couple[0] + insertion, 0) + count
        )
        poly_temp[insertion + couple[1]] = (
            poly_temp.get(insertion + couple[1], 0) + count
        )
    polymer = copy.deepcopy(poly_temp)


def get_char_count(polymers):
    chars = {}
    for poly, count in polymers.items():
        chars[poly[0]] = chars.get(poly[0], 0) + count
    chars[template[-1:]] += 1
    return chars


chars = get_char_count(polymer)
max_val = chars[max(chars, key=chars.get)]
min_val = chars[min(chars, key=chars.get)]

print(f"{max_val-min_val}")
