from collections import Counter


class Problem:
    def __init__(self):
        self.listA: list[int] = []
        self.listB: list[int] = []

    def parse(self, path: str):
        with open(path) as fp:
            while True:
                line = fp.readline()

                if not line:
                    break

                split = line.split('   ')
                self.listA.append(int(split[0]))
                self.listB.append(int(split[1]))

    def part1(self) -> int:
        a = sorted(self.listA)
        b = sorted(self.listB)
        sum = 0

        for i, x in enumerate(a):
            sum += abs(x - b[i])

        return sum

    def part2(self) -> int:
        freq = Counter(self.listB)
        sum = 0

        for x in self.listA:
            sum += x * freq[x]

        return sum
