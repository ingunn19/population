"""

    To-do
- ask for filename -x-
- open file -x-
- stop program if file does not exist -x-
- ask for year to check -x-
- read file -x-
- split text into list by newline (lines) -x-
- split items in list to list by spaces (columns) -x-
- check if year is valid -x-
- if year is not available error message and ask again -x-
- gather population numbers under designated year
- find min and max population numbers
- create touple (min number, state)
- create touple (max number, state)
- print

"""



def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        print("Filename", filename, "not found!")
        return False


def list_lines(file_object):
    lines = [(line.replace(" ", "", 1)).strip() for line in file_object]
    return lines


def split_columns(lines):
    columns = [column.split() for column in lines]
    return columns


def check_year(columns, year):
    try:
        year_to_check = columns[0].index(year)
    except ValueError:
        print("Invalid year!")
        year = input("Enter year:")
    return year_to_check


def gather_numbers(columns, year_to_check):
    numbers = []
    for i in range (1, len(columns)):
        numbers.append(columns[i] [year_to_check])
    return numbers

#...

def print_test(numbers):
    print(numbers)

#...


def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object:
        year = input("Enter year: ")
        lines = list_lines(file_object)
        columns = split_columns(lines)
        year_to_check = check_year(columns, year)
        numbers = gather_numbers(columns, year_to_check)
        print_test(numbers)


main()
