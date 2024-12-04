class Problem:
    def __init__(self):
        pass

    def parse(self, path: str):
        with open(path) as fp:
            while True:
                line = fp.readline()

                if not line:
                    break

    def part1(self) -> int:
        return 0

    def part2(self) -> int:
        return 0
