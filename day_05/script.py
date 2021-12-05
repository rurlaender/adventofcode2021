class point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class field:
    """Representing a area with hydrothermal vents"""

    area = []

    def __init__(self, size_x: int, size_y: int) -> None:
        """Initializes teh object with the given size

        Args:
            size_x (int): Size in x direction
            size_y (int): Size in y direction
        """
        for y in range(0, size_y):
            self.area.append([])
            for x in range(0, size_x):
                self.area[y].append(0)

    def __str__(self) -> str:
        """Visualizes the area

        Returns:
            str: the area as readable string
        """
        return_str = ""
        for line in self.area:
            for column in line:
                if column == 0:
                    return_str += "."
                else:
                    return_str += str(column)
            return_str += "\r\n"

        return return_str

    def insert_vents(self, start_pos: point, end_pos: point) -> None:
        # Check if line is horizontal or vertical
        orientation = 0  # 0 = horizontal, 1 = vertical, 2 diagonal
        if start_pos.x == end_pos.x:
            orientation = 1
        elif start_pos.x != end_pos.x and start_pos.y != end_pos.y:
            orientation = 2

        # calc start position an length
        start_x = 0
        length_x = 0
        start_y = 0
        length_y = 0
        if orientation == 0:
            # check which value is smaller
            if start_pos.x < end_pos.x:
                start_x = start_pos.x
                length_x = end_pos.x - start_pos.x
            else:
                start_x = end_pos.x
                length_x = start_pos.x - end_pos.x
        elif orientation == 1:
            # check which value is smaller
            if start_pos.y < end_pos.y:
                start_y = start_pos.y
                length_y = end_pos.y - start_pos.y
            else:
                start_y = end_pos.y
                length_y = start_pos.y - end_pos.y
        else:
            start_x = start_pos.x
            length_x = end_pos.x - start_pos.x
            start_y = start_pos.y
            length_y = end_pos.y - start_pos.y

            pass
        # input vents
        if orientation == 0:
            for x in range(start_x, start_x + length_x + 1):
                self.area[start_pos.y][x] += 1
        elif orientation == 1:
            for y in range(start_y, start_y + length_y + 1):
                self.area[y][start_pos.x] += 1
        else:
            if length_x < 0:
                iteration_x = -1
                iter_end_x = start_x + length_x - 1
            else:
                iteration_x = 1
                iter_end_x = start_x + length_x + 1

            if length_y < 0:
                iteration_y = -1
                iter_end_y = start_y + length_y - 1
            else:
                iteration_y = 1
                iter_end_y = start_y + length_y + 1
            count = 0
            for y in range(start_y, iter_end_y, iteration_y):
                self.area[y][start_x + count] += 1
                count += iteration_x

    def count_overlaping(self, limit: int) -> int:
        """Counts on how many position >= than limit lines overlap

        Args:
            limit (int): The limit for counting

        Returns:
            int: number of overlapping positions
        """
        counter = 0
        for line in self.area:
            for column in line:
                if column >= limit:
                    counter += 1
        return counter


def read_data(filename):
    points = []
    with open(filename, "r") as input_data:
        for line in input_data:
            start, stop = line.split(" -> ")
            x, y = start.split(",")
            start_point = point(int(x), int(y))
            x, y = stop.split(",")
            stop_point = point(int(x), int(y))
            points.append((start_point, stop_point))
    return points


lines = read_data("day_05/data.txt")
area = field(1000, 1000)
for line in lines:
    area.insert_vents(line[0], line[1])
print(area)
print(area.count_overlaping(2))
