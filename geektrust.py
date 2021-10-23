import sys


def readfile(input_file_name=None):
    """
    Reads inputs from argument or optionally input file (for testing) and
    returns optimal orbit and vehicle data that minimises ride time.

    Args:
        input_file_name (str, optional): Optionally reads input file
        (used only for testing). Defaults to None.
    """
    if not(input_file_name):
        input_file_name = sys.argv[-1]

    with open(input_file_name, "r") as input_file:
        input_list = input_file.readlines()[0].strip().split()

    return(input_list)


if __name__ == "__main__":
    readfile('input1.txt')
