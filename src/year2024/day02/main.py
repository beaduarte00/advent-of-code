import sys

from problem import Problem


def main():
    p = Problem()
    p.parse(sys.argv[1])

    print(p.part1(), p.part2(), sep='\n')


if __name__ == '__main__':
    main()
