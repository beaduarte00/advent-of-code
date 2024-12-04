import re


class Problem:
    def __init__(self):
        self.memory = ''

    def parse(self, path: str):
        with open(path) as fp:
            self.memory = fp.read()

    def part1(self) -> int:
        sum = 0

        for match in re.finditer(r"mul\((\d+),(\d+)\)", self.memory, re.MULTILINE):
            sum += int(match.group(1)) * int(match.group(2))

        return sum

    def part2(self) -> int:
        sum = 0
        do = True

        for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", self.memory, re.MULTILINE):
            group = match.group(0)

            if group == 'do()':
                do = True
            elif group == "don't()":
                do = False
            elif do:
                sum += int(match.group(1)) * int(match.group(2))

        return sum
