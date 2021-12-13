def get_data(filename):
    lines = []
    with open(filename, "r") as data:
        for line in data:
            lines.append(line.rstrip("\n"))
    return lines


open_chars = "(<[{"
close_chars = [")", ">", "]", "}"]
lines = get_data("day_10/data.txt")
result = 0
result2 = []
cost = {")": 3, "]": 57, "}": 1197, ">": 25137}
cost_corrupt = {"(": 1, "[": 2, "{": 3, "<": 4}
for line in lines:
    open_lst = []
    for i in range(0, len(line)):
        if line[i] in open_chars:
            open_lst.append(line[i])
        else:
            # check if the last character is the the opening one
            search_char = ""
            if line[i] == ")":
                search_char = "("
            elif line[i] == ">":
                search_char = "<"
            elif line[i] == "]":
                search_char = "["
            elif line[i] == "}":
                search_char = "{"
            if open_lst[len(open_lst) - 1] != search_char:
                result += cost[line[i]]
                break
            else:
                open_lst.pop()
    if i == len(line) - 1:
        line_cost = 0
        char = ""
        for _ in range(0, len(open_lst)):
            line_cost = line_cost * 5 + cost_corrupt[open_lst.pop()]
        result2.append(line_cost)


print(result)
result2.sort()
print(result2[int(((len(result2) - 1) / 2))])
