INPUT_FILE = 'day02.txt'


points = {
    'A': 1,
    'B': 2,
    'C': 3
}

rules = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

stats = {
    'LOSS': 0,
    'DRAW': 3,
    'WIN': 6
}


def part1():
    moves = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    with open(INPUT_FILE) as games:
        score = 0

        for game in games:
            guest = game[0]
            home = moves[game[2]]

            if rules[guest] == home:
                score += stats['LOSS']
            elif guest == home:
                score += stats['DRAW']
            else:
                score += stats['WIN']

            score += points[home]

    return score


def part2():
    outcomes = {
        'X': 'LOSS',
        'Y': 'DRAW',
        'Z': 'WIN'
    }

    with open(INPUT_FILE) as games:
        score = 0

        for game in games:
            guest = game[0]
            game = game[2]
            home = ''

            if game == 'X':
                home = rules[guest]
            elif game == 'Y':
                home = guest
            else:
                for move in rules.keys():
                    if rules[move] == guest:
                        home = move

            score += points[home]
            score += stats[outcomes[game]]

    return score


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
