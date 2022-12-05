import re


INPUT_FILE = 'day04.txt'
PATTERN = '(\\d+)-(\\d+),(\\d+)-(\\d+)'


pattern = re.compile(PATTERN)


def part1():
    answer = 0

    with open(INPUT_FILE) as pairs:
        for pair in pairs.readlines():
            a, b, c, d = pattern.findall(pair)[0]

            if int(a) <= int(c) <= int(d) <= int(b) \
                or int(c) <= int(a) <= int(b) <= int(d):
                answer += 1

    return answer


def part2():
    answer = 0

    with open(INPUT_FILE) as pairs:
        for pair in pairs.readlines():
            a, b, c, d = pattern.findall(pair)[0]

            if int(a) <= int(c) <= int(d) <= int(b) \
                or int(c) <= int(a) <= int(b) <= int(d) \
                    or int(a) <= int(c) <= int (b) \
                        or int(c) <= int(a) <= int(d):
                answer += 1

    return answer


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
