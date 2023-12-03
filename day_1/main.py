
def get_total():
    list_of_numbers = []
    with open("input.txt", "r") as f:
        for line in f.readlines():
            numbers_in_current_line = []
            for char in line:
                if char.isnumeric():
                    numbers_in_current_line.append(char)
            number = numbers_in_current_line[0] + numbers_in_current_line[-1]
            list_of_numbers.append(int(number))

    return sum(list_of_numbers)


def main():
    print(f"The total is {get_total()}")


if __name__ == "__main__":
    main()