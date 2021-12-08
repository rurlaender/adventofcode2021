import math


class seven_seg:
    def __init__(self, pattern, digits) -> None:
        self.patterns = []
        self.digits = []

        for pat in pattern:
            self.patterns.append("".join(sorted(pat)))
            self.patterns.sort(key=len)
        for digit in digits:
            self.digits.append("".join(sorted(digit)))

    def sub_str(self, str_a: str, str_b: str) -> str:
        ret_str = ""
        for x in str_b:
            if x not in str_a:
                ret_str += x
        return ret_str

    def find_pattern(self) -> None:
        numbers = [-1, 0, -1, -1, 2, -1, -1, 1, 9, -1]
        # Find segment a
        self.mapping = {}
        self.mapping["a"] = self.sub_str(self.patterns[0], self.patterns[1])
        # find the 3
        for i in range(3, 6):
            if len(self.sub_str(self.patterns[1], self.patterns[i])) == 2:
                numbers[3] = i
        self.mapping["b"] = self.sub_str(self.patterns[numbers[3]], self.patterns[2])
        # find 5 and 2
        for i in range(3, 6):
            if numbers[3] != i:
                if len(self.sub_str(self.mapping["b"], self.patterns[i])) != len(
                    self.patterns[i]
                ):
                    numbers[5] = i
                else:
                    numbers[2] = i
        # get segment e
        self.mapping["e"] = self.sub_str(
            self.patterns[numbers[3]], self.patterns[numbers[2]]
        )
        # get segment g
        temp = self.sub_str(self.patterns[numbers[4]], self.patterns[numbers[3]])
        self.mapping["g"] = self.sub_str(self.mapping["a"], temp)
        # get segment d
        temp = self.sub_str(self.mapping["a"], self.patterns[numbers[3]])
        temp = self.sub_str(self.mapping["g"], temp)
        self.mapping["d"] = self.sub_str(self.patterns[numbers[1]], temp)
        # get segment f
        temp = self.sub_str(self.mapping["a"], self.patterns[numbers[5]])
        temp = self.sub_str(self.mapping["b"], temp)
        temp = self.sub_str(self.mapping["d"], temp)
        self.mapping["f"] = self.sub_str(self.mapping["g"], temp)
        # get segment c
        self.mapping["c"] = self.sub_str(self.mapping["f"], self.patterns[numbers[1]])
        # Switch key val
        self.mapping = {self.mapping[k]: k for k in self.mapping}

    def str_to_nbr(self, str) -> int:
        if str == "cf":
            return 1
        elif str == "acdeg":
            return 2
        elif str == "acdfg":
            return 3
        elif str == "bcdf":
            return 4
        elif str == "abdfg":
            return 5
        elif str == "abdefg":
            return 6
        elif str == "acf":
            return 7
        elif str == "abcdefg":
            return 8
        elif str == "abcdfg":
            return 9
        else:
            return 0

    def convert(self) -> None:
        for i in range(0, 4):
            temp = ""
            for nbr in range(0, len(self.digits[i])):
                temp += self.mapping[self.digits[i][nbr]]
            self.digits[i] = "".join(sorted(temp))

    def get_all_numbers(self) -> int:
        self.find_pattern()
        self.convert()
        result = 0
        for i in range(0, 4):
            result += int(self.str_to_nbr(self.digits[i]) * math.pow(10, 3 - i))
        return result

    def get_simple_numbers(self) -> int:
        numbers = 0
        for nbr in self.digits:
            if len(nbr) == 2 or len(nbr) == 4 or len(nbr) == 3 or len(nbr) == 7:
                numbers += 1
        return numbers


def read_data(filename):
    resp_data = []
    with open(filename, "r") as data:
        for line in data:
            pattern, digits = line.split(" | ")
            resp_data.append(
                seven_seg(pattern.split(" "), digits.rstrip("\n").split(" "))
            )
    return resp_data


result = 0
for nbrs in read_data("day_08/data.txt"):
    result += nbrs.get_simple_numbers()
print(f"The result for part one is: {result}")

result = 0
for nbrs in read_data("day_08/data.txt"):
    result += nbrs.get_all_numbers()
print(f"The result for part one is: {result}")
