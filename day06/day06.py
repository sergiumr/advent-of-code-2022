INPUT_FILE = 'day06.txt'


def parse_file(unique_size):
    answer = 0
    queue = []

    with open(INPUT_FILE) as message:
        for x in message.readline():
            queue.append(x)
            answer += 1

            if len(queue) != unique_size:
                continue

            if len(set(queue)) == len(queue):
                break
            
            queue = queue[1:]

    return answer


def part1():
    UNIQUE_SIZE = 4

    return parse_file(UNIQUE_SIZE)


def part2():
    UNIQUE_SIZE = 14

    return parse_file(UNIQUE_SIZE)


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
