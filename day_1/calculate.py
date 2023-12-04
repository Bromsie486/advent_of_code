
def get_total():
    list_of_numbers = []
    numbers_as_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    letter_replacements = ["o1e", "t2o", "t3e", "f4r", "f5e", "s6x", "s7n", "e8t", "n9e"]
    with open("input.txt", "r") as f:
        for line in f.readlines():
            numbers_in_current_line = []
            print(f"original line: {line}")
            for index, num in enumerate(numbers_as_letters):
                if num in line:
                    line = line.replace(num, letter_replacements[index])
            print(f"modified line: {line}")

            for char in line:
                if char.isnumeric():
                    numbers_in_current_line.append(char)
            number = numbers_in_current_line[0] + numbers_in_current_line[-1]
            list_of_numbers.append(int(number))

    return sum(list_of_numbers)


def main():
    print(f"The total is {get_total()}")
    #get_total()


if __name__ == "__main__":
    main()