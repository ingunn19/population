#To-do
#ask for filename
#ask for year to check
#open file
#read file
#split text into list by newline (lines)
#split items in list to list by spaces (columns)
#check if year is valid
#if year is not available error message and ask again
#find min and max population numbers
#create touple (min number, state)
#create touple (max number, state)
#print



def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        print("Filename", filename, "not found!")
        return False


def list_lines(file_object):
    lines = [line.strip() for line in file_object]
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


#...

def print_test(year_to_check):
    print(year_to_check)

#...


def main():
    filename = input("Enter filename: ")
    file_object = open_file(filename)
    if file_object:
        year = input("Enter year: ")
        lines = list_lines(file_object)
        columns = split_columns(lines)
        year_to_check = check_year(columns, year)
        print_test(year_to_check)


main()
