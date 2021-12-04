import math


class bcolors:
    OK = "\033[92m"  # GREEN
    WARNING = "\033[93m"  # YELLOW
    FAIL = "\033[91m"  # RED
    RESET = "\033[0m"  # RESET COLOR


class bingo:
    """
    Class representing a bingo board
    Only horizontal or vertical lines count
    """

    def __str__(self) -> str:
        ret_str = ""
        for y in range(0, 5):
            for x in range(0, 5):
                if self.match[y][x] == True:
                    ret_str += bcolors.OK + f"{self.board[y][x]:2d}" + " "
                else:
                    ret_str += bcolors.RESET + f"{self.board[y][x]:2d}" + " "
            ret_str += "\r\n"
        ret_str += bcolors.RESET
        return ret_str

    def __init__(self, data) -> None:
        self.board = data
        self.match = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

    def check_bingo(self) -> bool:
        # Check horizontal
        for y in range(0, 5):
            if (
                self.match[y][0]
                == self.match[y][1]
                == self.match[y][2]
                == self.match[y][3]
                == self.match[y][4]
                == True
            ):
                return (True, 0, y)
        # Check vertical
        for x in range(0, 5):
            if (
                self.match[0][x]
                == self.match[1][x]
                == self.match[2][x]
                == self.match[3][x]
                == self.match[4][x]
                == True
            ):
                return (True, 1, x)
        return (False, 0, 0)

    def add_number(self, number: int) -> bool:
        for y in range(0, 5):
            for x in range(0, 5):
                if self.board[y][x] == number:
                    self.match[y][x] = True
                    break

        return self.check_bingo()

    def calc(self, orientation, line) -> int:
        ret_val = 0
        for y in range(0, 5):
            for x in range(0, 5):
                if self.match[y][x] == False:
                    ret_val += self.board[y][x]
        return ret_val


nbrs = []
boards = []

with open("day_04/data.txt", "r") as data:
    board = 0
    y = 0
    board_nbrs = []
    for index, line in enumerate(data):
        if index == 0:
            str_nbrs = line.split(",")
            for nbr in str_nbrs:
                nbrs.append(int(nbr))
        if (index - 1) % 6 == 0 and index > 1:
            y = 0
            boards.append(bingo(board_nbrs))
            board += 1
            board_nbrs = []
        elif index >= 2:
            str_nbrs = line.lstrip().replace("  ", " ").split(" ")
            for i, nbr in enumerate(str_nbrs):
                if i == 0:
                    board_nbrs.append([])
                board_nbrs[y].append(int(nbr))
            y += 1
    boards.append(bingo(board_nbrs))


for nbr in nbrs:
    for board in boards:
        result, orientation, pos = board.add_number(nbr)
        if result == True:
            print(result, orientation, pos, nbr)
            print(board)

            print(board.calc(orientation, pos))
            print(board.calc(orientation, pos) * nbr)
            break
    else:
        continue
    break

# for board in boards:
#    print(board)

for nbr in nbrs:
    copy_boards = boards[:]
    for index, board in enumerate(boards):
        result, orientation, pos = board.add_number(nbr)
        if result == True:
            # print(result, orientation, pos, nbr)
            # print(board)

            # print(board.calc(orientation, pos))
            # print(board.calc(orientation, pos) * nbr)
            if len(boards) == 1:
                # final board

                print(board)
                print(board.calc(orientation, pos), nbr)
                print(board.calc(orientation, pos) * nbr)
                break
            else:
                copy_boards.remove(board)
    else:
        boards = copy_boards[:]
        continue
    break
