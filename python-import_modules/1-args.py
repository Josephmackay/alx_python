import sys

number_of_arguments = len(sys.argv)

if number_of_arguments == 1:
    print("1 argument")
    print("1: {}".format(sys.argv[1]))
elif number_of_arguments == 2:
    print("2 arguments:")
    print("1: {}".format(sys.argv[1]))
    print("2: {}".format(sys.argv[2]))
elif number_of_arguments == 3:
    # Handle three argument case
    print("3 arguments:")
    print("1: {}".format(sys.argv[1]))
    print("2: {}".format(sys.argv[2]))
    print("3: {}".format(sys.argv[3]))
else:
    print("Unexpected number of arguments: {}".format(number_of_arguments))
    # Handle unexpected arguments
if __name__ == "__main__":
    pass        