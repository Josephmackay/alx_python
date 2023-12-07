import sys

number_of_arguments = len(sys.argv)

if number_of_arguments == 1:
    # Handle single argument case
    print("Number of argument(s): 0.")
elif number_of_arguments == 2:
    # Handle two argument case
    print(f"Number of argument: {number_of_arguments}.")
    print(f"1: {sys.argv[1]}")
    print(f"2: {sys.argv[2]}")
else:
    print(f"Unexpected number of arguments: {number_of_arguments}")
    # Handle unexpected arguments
if __name__ == "__main__":
    pass        