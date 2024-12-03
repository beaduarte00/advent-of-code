class Problem:
    def __init__(self):
        self.matrix: list[list[int]] = []

    def parse(self, path: str):
        with open(path) as fp:
            while True:
                line = fp.readline()

                if not line:
                    break

                split = line.split(' ')
                self.matrix.append([int(x) for x in split])

    def isSafe(self, row: list[int]) -> bool:
        lastdiff = 0

        for i in range(len(row) - 1):
            diff = row[i] - row[i + 1]
            absdiff = abs(diff)

            if absdiff < 1 or absdiff > 3 or diff * lastdiff < 0:
                return False

            lastdiff = diff

        return True

    def isDampenerSafe(self, row: list[int]) -> bool:
        if self.isSafe(row):
            return True

        for i in range(len(row)):
            copy = [x for j, x in enumerate(row) if i != j]

            if self.isSafe(copy):
                return True

        return False

    def part1(self) -> int:
        sum = 0

        for row in self.matrix:
            sum += self.isSafe(row)

        return sum

    def part2(self) -> int:
        sum = 0

        for row in self.matrix:
            sum += self.isDampenerSafe(row)

        return sum
