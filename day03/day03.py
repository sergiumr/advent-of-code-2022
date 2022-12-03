INPUT_FILE = 'day03.txt'
ORDER_DIFFERENCE = 26
BADGE_GROUP = 3


def get_points(item):
    if item.islower():
        return ord(item) - ord('a') + 1

    return ord(item) - ord('A') + 1 + ORDER_DIFFERENCE


def part1():
    answer = 0

    with open(INPUT_FILE) as rucksack:
        for items in rucksack.readlines():
            objects = { }

            for i in range(len(items)// 2):
                objects[items[i]] = 1
                
            for i in range(len(items)// 2, len(items)):
                if objects.get(items[i]) is None:
                    continue

                answer += get_points(items[i])
                break

    return answer


def part2():
    objects = { 
        1: { },
        2: { },
        3: { }
    }
    answer = 0
    crt_line = 1

    with open(INPUT_FILE) as rucksack:
        for items in rucksack.readlines(): 
            for item in items:
                if item != '\n':
                    objects[crt_line][item] = 1

            if (crt_line - 0) % BADGE_GROUP == 0:
                answer += get_points((objects[1].keys() & objects[2].keys() & objects[3].keys()).pop())
                
                objects = { 
                    1: { },
                    2: { },
                    3: { }
                }

                crt_line = 0

            crt_line += 1

    return answer


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
