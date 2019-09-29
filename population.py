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
- gather population numbers under designated year -x-
- find min and max population numbers -x-
- create touple (min number, state) -x-
- create touple (max number, state) -x-
- print -x-

"""



def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        print("Filename", filename, "not found!")
        return False


def list_lines(file_object):
    lines = [(line.replace(" ", "_", 1)).strip() for line in file_object]
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


def state_year(columns, year_to_check):
    state_pop = [(int(columns[i][year_to_check]), ((columns[i][0]).replace("_", " ")).strip()) for i in range(1, len(columns))]
    return state_pop


def min_max(state_pop):
    state_pop = sorted(state_pop)
    min_pop = state_pop[0]
    max_pop = state_pop[-1]
    return min_pop, max_pop


def printing(min_pop, max_pop):
    print("Minimum:", min_pop)
    print("Maximum:", max_pop)


def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object:
        year = input("Enter year: ")
        lines = list_lines(file_object)
        columns = split_columns(lines)
        year_to_check = check_year(columns, year)
        state_pop = state_year(columns, year_to_check)
        min_pop, max_pop = min_max(state_pop)
        printing(min_pop, max_pop)
        file_object.close()


main()
