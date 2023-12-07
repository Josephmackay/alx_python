import sys

number_of_arguments = len(sys.argv)

if number_of_arguments == 1:
    print("Number of argument(s): 0.")
elif number_of_arguments == 2:
    print("2 arguments:")
    print(f"1: {sys.argv[1]}")
    print(f"2: {sys.argv[2]}")
elif number_of_arguments == 3:
    # Handle three argument case
    print("3 arguments:")
    print(f"1: {sys.argv[1]}")
    print(f"2: {sys.argv[2]}")
    print(f"3: {sys.argv[3]}")
else:
    print(f"Unexpected number of arguments: {number_of_arguments}")
    # Handle unexpected arguments
if __name__ == "__main__":
    pass        