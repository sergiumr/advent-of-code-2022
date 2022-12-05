import re

INPUT_FILE = 'day05.txt'
PATTERN = 'move (\\d+) from (\\d+) to (\\d+)'
pattern = re.compile(PATTERN)


def part1():
    answer = ''
    crates = {}
    read_crates = True
    swap_crates = False

    with open(INPUT_FILE) as supplies:
        for line in supplies.readlines():
            if line == '\n' or line[1].isdigit():
                read_crates = False

                if not swap_crates:
                    for i in crates.keys():
                        crates[i] = crates[i][::-1]

                    swap_crates = True

                continue

            if read_crates:
                for i in range(1, len(line), 4):
                    if line[i] == ' ':
                        continue

                    crt_crate = (i - 1) // 4 + 1
                    crates[crt_crate] = crates.get(crt_crate, []) + [line[i]]
            else:
                count, source, target = [int(x) for x in pattern.findall(line)[0]]
                for i in range(count):
                    crates[target].append(crates[source].pop())

    for i in range(1, max(crates.keys()) + 1):
        answer += crates[i][-1]

    return answer


def part2():
    answer = ''
    crates = {}
    read_crates = True
    swap_crates = False

    with open(INPUT_FILE) as supplies:
        for line in supplies.readlines():
            if line == '\n' or line[1].isdigit():
                read_crates = False

                if not swap_crates:
                    for i in crates.keys():
                        crates[i] = crates[i][::-1]

                    swap_crates = True

                continue

            if read_crates:
                for i in range(1, len(line), 4):
                    if line[i] == ' ':
                        continue

                    crt_crate = (i - 1) // 4 + 1
                    crates[crt_crate] = crates.get(crt_crate, []) + [line[i]]
            else:
                count, source, target = [int(x) for x in pattern.findall(line)[0]]
                new_crates = []

                for i in range(count):
                    new_crates = [crates[source].pop()] + new_crates

                crates[target] = crates[target] + new_crates[::1]

    for i in range(1, max(crates.keys()) + 1):
        answer += crates[i][-1]

    return answer


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')


if __name__ == '__main__':
    main()
