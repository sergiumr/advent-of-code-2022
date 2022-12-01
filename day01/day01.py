INPUT_FILE = 'day01.txt'


def part1():
    max_calories = 0

    with open(INPUT_FILE) as nums:
        current_calories = 0

        for num in nums:
            if num != '\n':
                current_calories += int(num)
            else:
                max_calories = max(max_calories, current_calories)
                current_calories = 0

    return max_calories


def part2():
    max1 = 0
    max2 = 0
    max3 = 0

    with open(INPUT_FILE) as nums:
        current_calories = 0

        for num in nums:
            if num != '\n':
                current_calories += int(num)
            else:
                if current_calories > max1:
                    max3, max2, max1 = max2, max1, current_calories
                elif current_calories > max2:
                    max3, max2 = max2, current_calories
                elif current_calories > max3:
                    max3 = current_calories

                current_calories = 0

    return max1 + max2 + max3


def main():
    print(f'Answer #1: {part1()}')

    print(f'Answer #2: {part2()}')
        

if __name__ == '__main__':
    main()
